import os
import json
import requests
import sys
import time
import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(__file__), '..', 'logs', 'llm_calls.log')),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Ensure logs directory exists
os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'logs'), exist_ok=True)

# Optional: Try to import Google Generative AI library
try:
    import google.generativeai as genai
    HAS_GOOGLE_LIB = True
except ImportError:
    HAS_GOOGLE_LIB = False

def ask_llm(prompt, task_type='general_tasks', model_override=None):
    """
    Calls an LLM provider based on the task_type defined in model-router.json.
    Supports Google, Groq, OpenRouter, and Ollama with retry logic and fallback.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    router_path = os.path.join(script_dir, '..', 'model-router.json')
    
    if not os.path.exists(router_path):
        logger.error(f"model-router.json not found at {router_path}")
        return f"Error: model-router.json not found at {router_path}"
    
    try:
        with open(router_path, 'r', encoding='utf-8') as f:
            router_data = json.load(f)
    except Exception as e:
        logger.error(f"Error reading model-router.json: {e}")
        return f"Error reading model-router.json: {e}"

    # Find the primary routing rule
    routing_rule = next((rule for rule in router_data.get('routing_rules', []) if rule.get('task_type') == task_type), None)
    
    if not routing_rule:
        logger.warning(f"Task type '{task_type}' not found in router. Defaulting to general_tasks.")
        routing_rule = next((rule for rule in router_data.get('routing_rules', []) if rule.get('task_type') == 'general_tasks'), None)
        if not routing_rule:
            routing_rule = router_data.get('routing_rules', [{}])[0]

    provider = routing_rule.get('provider')
    model = model_override if model_override else routing_rule.get('model')

    logger.info(f"Using provider: {provider}, model: {model} for task: {task_type}{' (OVERRIDDEN)' if model_override else ''}")
    response = call_with_retry(prompt, provider, model)

    # If primary fails, try fallback if it's not already ollama and not overridden
    if not model_override and ("Error" in response or "rate limit" in response.lower()) and provider != 'ollama':
        fallback_rule = next((rule for rule in router_data.get('routing_rules', []) if rule.get('task_type') == 'fallback'), None)
        if fallback_rule:
            logger.warning(f"Primary provider {provider} failed. Attempting fallback to {fallback_rule.get('provider')}...")
            response = call_with_retry(prompt, fallback_rule.get('provider'), fallback_rule.get('model'))

    return response

def call_with_retry(prompt, provider, model, max_retries=3):
    delay = 2
    last_error = ""
    
    for i in range(max_retries):
        try:
            if provider == 'google':
                res = call_google(prompt, model)
            elif provider == 'groq':
                res = call_groq(prompt, model)
            elif provider == 'openrouter':
                res = call_openrouter(prompt, model)
            elif provider == 'ollama':
                res = call_ollama(prompt, model)
            else:
                return f"Error: Unsupported provider '{provider}'"
            
            # Check for rate limit or transient errors in the response string
            if isinstance(res, str) and ("429" in res or "rate limit" in res.lower() or "503" in res):
                last_error = res
                logger.warning(f"Retry {i+1}/{max_retries} due to rate limit/error: {res}")
                time.sleep(delay + random.uniform(0, 1))
                delay *= 2
                continue
            
            return res
        except Exception as e:
            last_error = str(e)
            logger.error(f"Attempt {i+1} failed for {provider}/{model}: {e}")
            time.sleep(delay + random.uniform(0, 1))
            delay *= 2
            
    return f"Error: {provider} failed after {max_retries} attempts. Last error: {last_error}"

def call_google(prompt, model):
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        return "Error: GOOGLE_API_KEY not set."
    
    # Use v1 for stable flagship models (Gemini 3.1)
    if HAS_GOOGLE_LIB:
        try:
            genai.configure(api_key=api_key)
            # Ensure model name is correctly formatted for SDK
            model_name = model if 'models/' in model else f"models/{model}"
            gemini = genai.GenerativeModel(model_name)
            response = gemini.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e): return "Error: Google 429 Rate Limit"
            logger.error(f"Google API error: {e}")
            return f"Google API error: {e}"
    else:
        # Standardize model path for REST - Using v1 for 2026 flagship support
        model_id = model.replace('models/', '')
        url = f"https://generativelanguage.googleapis.com/v1/models/{model_id}:generateContent?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 429: return "Error: Google 429 Rate Limit"
            if response.status_code != 200:
                # Fallback to v1alpha if v1 fails for preview models
                url = f"https://generativelanguage.googleapis.com/v1alpha/models/{model_id}:generateContent?key={api_key}"
                response = requests.post(url, headers=headers, json=payload, timeout=60)
                if response.status_code != 200:
                    return f"Error: Google API (v1/v1alpha) returned status {response.status_code}: {response.text}"
            
            response.raise_for_status()
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            logger.error(f"Google Raw API error: {e}")
            return f"Google Raw API error: {e}"

def call_groq(prompt, model):
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        return "Error: GROQ_API_KEY not set."
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        if response.status_code == 429: return "Error: Groq 429 Rate Limit"
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        logger.error(f"Groq API error: {e}")
        return f"Groq API error: {e}"

def call_openrouter(prompt, model):
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        return "Error: OPENROUTER_API_KEY not set."
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/GraciaAutonoma",
        "X-Title": "Gracia Autonoma"
    }
    
    # Optimization for DeepSeek and Qwen: specific headers or parameters
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "top_p": 0.9,
        "temperature": 0.7
    }
    
    # Enable reasoning for reasoning-capable models (DeepSeek R1/V4, etc.)
    if any(m in model.lower() for m in ["deepseek-r1", "deepseek-v4"]):
        payload["include_reasoning"] = True

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        if response.status_code == 429: return "Error: OpenRouter 429 Rate Limit"
        if response.status_code != 200:
            return f"Error: OpenRouter API returned status {response.status_code}: {response.text}"
        response.raise_for_status()
        result = response.json()
        
        # Handle reasoning content if available
        message = result['choices'][0]['message']
        content = message.get('content', '')
        reasoning = message.get('reasoning', '')
        
        if reasoning:
            return f"<thought>\n{reasoning}\n</thought>\n\n{content}"
        return content
    except Exception as e:
        logger.error(f"OpenRouter API error: {e}")
        return f"OpenRouter API error: {e}"

def call_ollama(prompt, model):
    url = "http://localhost:11434/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        return response.json().get('response', '')
    except Exception as e:
        logger.error(f"Ollama error: {e}")
        return f"Ollama error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        # Usage: python llm_helper.py <task_type> <prompt>
        print(ask_llm(" ".join(sys.argv[2:]), task_type=sys.argv[1]))
    elif len(sys.argv) > 1:
        print(ask_llm(sys.argv[1]))
    else:
        print("Usage: python llm_helper.py [task_type] <prompt>")
