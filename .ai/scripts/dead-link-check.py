import re
from pathlib import Path

VAULT_ROOT = Path(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LOG_FILE = VAULT_ROOT / ".ai" / "logs" / "dead-links.log"

def check_dead_links():
    print(f"Checking for dead links in {VAULT_ROOT}...")
    
    # 1. Map all existing markdown files
    all_notes = {}
    for md_file in VAULT_ROOT.rglob("*.md"):
        all_notes[md_file.stem.lower()] = md_file
    
    dead_links = []
    
    # 2. Scan all files for [[WikiLinks]]
    for md_file in VAULT_ROOT.rglob("*.md"):
        if ".obsidian" in str(md_file) or ".git" in str(md_file):
            continue
            
        with open(md_file, "r", encoding="utf-8") as f:
            try:
                content = f.read()
            except UnicodeDecodeError:
                continue # Skip binary or badly encoded files
        
        # Match [[Link]] or [[Link|Alias]]
        links = re.findall(r"\[\[(.*?)\]\]", content)
        
        for link in links:
            # Extract the actual note name (before |)
            note_name = link.split("|")[0].strip()
            
            # Handle cases with paths like [[Folder/Note]]
            note_stem = Path(note_name).stem.lower()
            
            if note_stem not in all_notes:
                # Also check if the full path (relative to vault) exists
                # e.g. [[01-Projects/Graxia-OS/MAS-War-Room]]
                full_path_check = VAULT_ROOT / f"{note_name}.md"
                if not full_path_check.exists():
                    dead_links.append({
                        "file": str(md_file.relative_to(VAULT_ROOT)),
                        "link": link
                    })

    if dead_links:
        print(f"Found {len(dead_links)} dead links.")
        log_dir = LOG_FILE.parent
        log_dir.mkdir(parents=True, exist_ok=True)
        
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("# Dead Link Report\n\n")
            for entry in dead_links:
                f.write(f"- File: `{entry['file']}` -> Link: `[[{entry['link']}]]` (Broken)\n")
        print(f"Report saved to {LOG_FILE}")
    else:
        print("No dead links found. System integrity verified.")

if __name__ == "__main__":
    check_dead_links()
