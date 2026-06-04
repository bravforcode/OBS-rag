import os
import time
import subprocess
import datetime

# Configuration
VAULT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUEUE_PATH = os.path.join(VAULT_PATH, "01-Projects", "Graxia-OS", "Autonomous_Queue")
INBOX_PATH = os.path.join(VAULT_PATH, "00-Inbox")
LOG_PATH = os.path.join(VAULT_PATH, ".ai", "logs", "autonoma.log")
LOOP_SCRIPT = os.path.join(VAULT_PATH, ".ai", "scripts", "autonomous-loop.py")

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    print(log_entry.strip())
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(log_entry)

def check_queue():
    tasks = []
    if os.path.exists(QUEUE_PATH):
        for file in os.listdir(QUEUE_PATH):
            if file.endswith(".md"):
                tasks.append(os.path.join(QUEUE_PATH, file))
    return tasks

def check_inbox():
    tasks = []
    if os.path.exists(INBOX_PATH):
        for file in os.listdir(INBOX_PATH):
            if "URGENT" in file.upper() or "EXECUTE" in file.upper():
                tasks.append(os.path.join(INBOX_PATH, file))
    return tasks

def main():
    log_message("Sentinel Service started.")
    while True:
        try:
            tasks = check_queue() + check_inbox()
            
            for task_path in tasks:
                log_message(f"Found task: {task_path}")
                # Execute the autonomous loop script
                try:
                    subprocess.run(["python", LOOP_SCRIPT, task_path], check=True)
                except subprocess.CalledProcessError as e:
                    log_message(f"Error executing task {task_path}: {e}")
                except Exception as e:
                    log_message(f"Unexpected error for task {task_path}: {e}")
            
            time.sleep(60)
        except KeyboardInterrupt:
            log_message("Sentinel Service stopped by user.")
            break
        except Exception as e:
            log_message(f"Sentinel Service encountered an error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
