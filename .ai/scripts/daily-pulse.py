import os
import datetime
import subprocess

VAULT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INBOX_DIR = os.path.join(VAULT_PATH, "00-Inbox")
PROJECTS_DIR = r"C:\Users\menum" # Root where projects are

def get_git_activity():
    today = datetime.date.today().strftime("%Y-%m-%d")
    activity = []
    
    # Check some known repos
    repos = ["graxia os", "bravos"] # Example repos
    for repo in repos:
        repo_path = os.path.join(PROJECTS_DIR, repo)
        if os.path.exists(repo_path):
            try:
                cmd = f"git -C \"{repo_path}\" log --since=\"yesterday\" --oneline"
                output = subprocess.check_output(cmd, shell=True).decode()
                if output:
                    activity.append(f"### {repo}\n{output}")
            except:
                pass
    return "\n".join(activity)

def generate_pulse():
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    pulse_file = os.path.join(INBOX_DIR, f"Daily-Pulse-{date_str}.md")
    
    git_logs = get_git_activity()
    
    content = f"""---
type: pulse
date: {date_str}
---
# Daily Pulse - {date_str}

## Git Activity
{git_logs if git_logs else "No activity detected."}

## Vault Inbox Scan
- [ ] Review new items in {INBOX_DIR}

## Email Mock
- Check important threads in Sovereign Intelligence mailing list.

## Cognitive Load
- Current Focus: Phase 4 Implementation
"""
    
    if not os.path.exists(INBOX_DIR):
        os.makedirs(INBOX_DIR)
        
    with open(pulse_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated Daily Pulse: {pulse_file}")

if __name__ == "__main__":
    generate_pulse()
