import os
import re
from pathlib import Path

# Paths
VAULT_ROOT = Path(__file__).parent.parent.parent
INBOX_DIR = VAULT_ROOT / "00-Inbox"
HARVEST_DIR = VAULT_ROOT / "01-projects" / "graxia-os" / "harvested"
AI_MOC_PATH = VAULT_ROOT / "03-Resources" / "AI-Knowledge" / "AI-Master-MOC.md"

def harvest():
    print(f"Scanning {INBOX_DIR} for technical snippets...")
    
    if not INBOX_DIR.exists():
        print(f"Error: Inbox directory {INBOX_DIR} does not exist.")
        return

    if not HARVEST_DIR.exists():
        HARVEST_DIR.mkdir(parents=True, exist_ok=True)

    harvested_files = []

    for md_file in INBOX_DIR.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Regex to find python or bash blocks
        # Pattern: ```(python|bash)\n(.*?)\n```
        blocks = re.findall(r"```(python|bash)\n(.*?)\n```", content, re.DOTALL)
        
        if blocks:
            print(f"Found {len(blocks)} blocks in {md_file.name}")
            title = md_file.stem.replace(" ", "-").lower()
            
            for i, (lang, code) in enumerate(blocks):
                ext = ".py" if lang == "python" else ".sh"
                suffix = f"_{i}" if len(blocks) > 1 else ""
                harvested_filename = f"{title}{suffix}{ext}"
                harvested_path = HARVEST_DIR / harvested_filename
                
                with open(harvested_path, "w", encoding="utf-8") as hf:
                    hf.write(code)
                
                print(f"Harvested: {harvested_filename}")
                harvested_files.append({
                    "name": harvested_filename,
                    "lang": lang,
                    "source": md_file.name
                })

    if harvested_files:
        update_moc(harvested_files)

def update_moc(harvested_files):
    print(f"Updating AI Master MOC at {AI_MOC_PATH}")
    
    if not AI_MOC_PATH.exists():
        # Create it if it doesn't exist
        with open(AI_MOC_PATH, "w", encoding="utf-8") as f:
            f.write("# AI Master MOC\n\n## 🛠️ Harvested Technical Snippets\n\n| Snippet | Language | Source Note |\n|---------|----------|-------------|\n")

    with open(AI_MOC_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Ensure table header exists
    if "| Snippet | Language | Source Note |" not in content:
        if "## 🛠️ Harvested Technical Snippets" not in content:
            content += "\n\n## 🛠️ Harvested Technical Snippets\n\n| Snippet | Language | Source Note |\n|---------|----------|-------------|\n"
        else:
            content = content.replace("## 🛠️ Harvested Technical Snippets", "## 🛠️ Harvested Technical Snippets\n\n| Snippet | Language | Source Note |\n|---------|----------|-------------|\n")

    new_rows = ""
    for file in harvested_files:
        row = f"| {file['name']} | {file['lang']} | [[{file['source'].replace('.md', '')}]] |\n"
        if row not in content:
            new_rows += row

    if new_rows:
        # Append to the end of the file or find the table and append there.
        # For simplicity, we'll append to the end.
        with open(AI_MOC_PATH, "a", encoding="utf-8") as f:
            f.write(new_rows)
        print("MOC updated.")
    else:
        print("No new unique snippets to add to MOC.")

if __name__ == "__main__":
    harvest()
