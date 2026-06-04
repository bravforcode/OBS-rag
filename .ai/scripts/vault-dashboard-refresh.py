import subprocess
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
WELCOME_NOTE = VAULT_ROOT / "Welcome.md"

def get_recent_notes(count=5):
    notes = []
    for md_file in VAULT_ROOT.rglob("*.md"):
        if ".obsidian" in str(md_file) or ".git" in str(md_file):
            continue
        mtime = md_file.stat().st_mtime
        notes.append((mtime, md_file))
    
    # Sort by mtime descending
    notes.sort(key=lambda x: x[0], reverse=True)
    return notes[:count]

def get_git_commits(count=3):
    try:
        # Run git log command in the vault root
        result = subprocess.run(
            ["git", "log", f"-{count}", "--pretty=format:%h - %s (%cr)"],
            cwd=VAULT_ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split("\n")
    except Exception as e:
        return [f"Error fetching git commits: {e}"]

def refresh_dashboard():
    print(f"Refreshing dashboard {WELCOME_NOTE}...")
    
    recent_notes = get_recent_notes()
    commits = get_git_commits()
    
    # Read existing content
    if WELCOME_NOTE.exists():
        with open(WELCOME_NOTE, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "# Welcome to Project Gracia\n\n"

    # Create sections
    recent_section = "## 🕒 Recently Modified\n"
    for mtime, path in recent_notes:
        rel_path = path.relative_to(VAULT_ROOT)
        note_name = path.stem
        # Format date
        date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
        recent_section += f"- [[{note_name}]] _({date_str})_\n"

    git_section = "\n## 🚀 Last 3 Commits\n"
    for commit in commits:
        git_section += f"- {commit}\n"

    # We'll use marker tags to replace content or just append/overwrite
    # Better to overwrite specific markers if they exist, or just recreate the end.
    
    MARKER_START = "<!-- DASHBOARD_START -->"
    MARKER_END = "<!-- DASHBOARD_END -->"
    
    dashboard_content = f"{MARKER_START}\n{recent_section}{git_section}\n{MARKER_END}"
    
    if MARKER_START in content and MARKER_END in content:
        # Replace between markers
        import re
        new_content = re.sub(
            f"{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}",
            dashboard_content,
            content,
            flags=re.DOTALL
        )
    else:
        # Append to end
        new_content = content.rstrip() + "\n\n" + dashboard_content

    with open(WELCOME_NOTE, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("Dashboard refreshed successfully.")

if __name__ == "__main__":
    refresh_dashboard()
