import os
import sys
import subprocess
import shutil
import datetime
import json
import llm_helper

# Configuration
VAULT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DONE_PATH = os.path.join(VAULT_PATH, "01-Projects", "Graxia-OS", "Autonomous_Queue", "Done")
FAILED_PATH = os.path.join(VAULT_PATH, "01-Projects", "Graxia-OS", "Autonomous_Queue", "Failed")
LOG_PATH = os.path.join(VAULT_PATH, ".ai", "logs", "autonoma.log")
STRATEGIST_PATH = os.path.join(VAULT_PATH, ".claude", "agents", "strategist.md")
ARCHITECT_PATH = os.path.join(VAULT_PATH, ".claude", "agents", "architect.md")

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [LOOP] {message}\n"
    print(log_entry.strip())
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_entry)

def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def generate_plan(task_content, strategist_md, architect_md):
    """
    Generates a step-by-step execution plan using LLM.
    """
    log_message("Generating execution plan using Strategist and Architect personas via LLM...")
    
    prompt = f"""
SYSTEM CONTEXT:
STRATEGIST PERSONA:
{strategist_md}

ARCHITECT PERSONA:
{architect_md}

TASK TO EXECUTE:
{task_content}

INSTRUCTIONS:
You are an autonomous agent. Based on the task above and your personas, generate a list of shell commands to fulfill the task.
Return ONLY a JSON list of commands in the following format:
### COMMANDS: ["command1", "command2", ...]

Ensure the commands are safe and appropriate for a Windows environment.
"""

    response = llm_helper.ask_llm(prompt, task_type='high_reasoning')
    
    if response.startswith("Error"):
        log_message(f"LLM Helper returned error: {response}")
        return []

    plan = []
    try:
        if "### COMMANDS:" in response:
            json_part = response.split("### COMMANDS:")[1].strip()
            # Clean up potential markdown code blocks
            if json_part.startswith("```json"):
                json_part = json_part[7:]
            elif json_part.startswith("```"):
                json_part = json_part[3:]
            
            if json_part.endswith("```"):
                json_part = json_part[:-3]
            
            json_part = json_part.strip()
            
            # Find the first [ and last ] to extract the JSON list
            start_idx = json_part.find("[")
            end_idx = json_part.rfind("]") + 1
            if start_idx != -1 and end_idx != 0:
                json_str = json_part[start_idx:end_idx]
                plan = json.loads(json_str)
            else:
                log_message("Could not find JSON list in response.")
        else:
            log_message("LLM response did not contain '### COMMANDS:' marker.")
            log_message(f"Raw response preview: {response[:200]}...")
            
    except Exception as e:
        log_message(f"Error parsing LLM response: {e}")
        log_message(f"Raw response: {response}")

    return plan

def execute_command(command):
    max_retries = 3
    attempt = 0
    
    while attempt <= max_retries:
        if attempt > 0:
            log_message(f"Self-Correct Attempt {attempt}/{max_retries} for command: {command}")
        
        try:
            # Run command in Graxia OS path as default working dir if it exists
            cwd = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            if not os.path.exists(cwd):
                cwd = VAULT_PATH
                
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=cwd)
            log_message(f"Success: {command}")
            if result.stdout:
                log_message(f"Output: {result.stdout.strip()}")
            return True
        except subprocess.CalledProcessError as e:
            log_message(f"Failure: {command}")
            log_message(f"Error: {e.stderr.strip()}")
            attempt += 1
            if attempt > max_retries:
                log_message(f"Max retries reached for: {command}")
                return False
        except Exception as e:
            log_message(f"Unexpected error: {e}")
            return False
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python autonomous-loop.py <task_file_path>")
        sys.exit(1)

    task_path = sys.argv[1]
    log_message(f"Starting execution loop for: {task_path}")

    task_content = read_file(task_path)
    strategist_md = read_file(STRATEGIST_PATH)
    architect_md = read_file(ARCHITECT_PATH)

    if not task_content:
        log_message("Task file is empty or missing.")
        sys.exit(1)

    plan = generate_plan(task_content, strategist_md, architect_md)

    if not plan:
        log_message("Failed to generate a valid execution plan.")
        # Move to failed
        os.makedirs(FAILED_PATH, exist_ok=True)
        shutil.move(task_path, os.path.join(FAILED_PATH, os.path.basename(task_path)))
        sys.exit(1)

    all_success = True
    for cmd in plan:
        log_message(f"Executing: {cmd}")
        if not execute_command(cmd):
            all_success = False
            break

    # Cleanup
    if all_success:
        log_message("Task completed successfully.")
        os.makedirs(DONE_PATH, exist_ok=True)
        dest = os.path.join(DONE_PATH, os.path.basename(task_path))
        if os.path.exists(dest):
            dest = dest + "." + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.move(task_path, dest)
    else:
        log_message("Task failed execution.")
        os.makedirs(FAILED_PATH, exist_ok=True)
        dest = os.path.join(FAILED_PATH, os.path.basename(task_path))
        if os.path.exists(dest):
            dest = dest + "." + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.move(task_path, dest)

if __name__ == "__main__":
    main()
