import os
import sys
from llm_helper import ask_llm

def test_models():
    print("🚀 Starting 2026 Flagship Connectivity Test...\n")
    
    tasks = [
        ("strategic_planning", "As Gemini 3.1, what is your strategic outlook for AI in late 2026?"),
        ("deep_reasoning", "Using DeepSeek V4 reasoning, explain the implications of post-quantum cryptography on blockchain."),
        ("code_expert", "Write a highly optimized Rust implementation of a distributed lock manager."),
        ("general_tasks", "Summarize the key advantages of DeepSeek V4 Flash for real-time applications.")
    ]
    
    for task_type, prompt in tasks:
        print(f"Testing Task Type: {task_type}...")
        try:
            response = ask_llm(prompt, task_type=task_type)
            if "Error" in response:
                print(f"❌ FAILED: {response}\n")
            else:
                print(f"✅ SUCCESS:")
                # Print first 150 chars of response
                preview = response[:150].replace('\n', ' ') + "..."
                print(f"   Response: {preview}\n")
        except Exception as e:
            print(f"💥 CRITICAL ERROR testing {task_type}: {e}\n")

    # Test model_override with a 2026 model
    print("Testing model_override with 'gemini-3.1-flash'...")
    try:
        response = ask_llm("System status check.", task_type="general_tasks", model_override="gemini-3.1-flash")
        print(f"✅ Override Success: {response[:50]}...\n")
    except Exception as e:
        print(f"❌ Override Failed: {e}\n")

if __name__ == "__main__":
    # Add parent dir to path to import llm_helper if needed (though it's in the same dir)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    test_models()
