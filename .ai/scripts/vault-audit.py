import os
import re

VAULT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def audit():
    all_files = []
    links = set()
    
    # regex for obsidian links [[link]]
    link_pattern = re.compile(r'\[\[(.*?)\]\]')
    
    print(f"Auditing Vault: {VAULT_PATH}")
    
    for root, dirs, files in os.walk(VAULT_PATH):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, VAULT_PATH)
                # Note name without extension
                note_name = os.path.splitext(file)[0]
                all_files.append(note_name)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Check for metadata (frontmatter)
                        if not content.startswith("---"):
                            print(f"[MISSING METADATA] {rel_path}")
                        
                        # Find links
                        found_links = link_pattern.findall(content)
                        for link in found_links:
                            # Handle aliases [[Link|Alias]]
                            clean_link = link.split('|')[0].strip()
                            links.add(clean_link)
                except UnicodeDecodeError:
                    print(f"[ERROR] Could not decode {rel_path} - possibly binary or different encoding.")

    # Find orphans
    orphans = set(all_files) - links
    print(f"\n--- Orphan Notes ({len(orphans)}) ---")
    for orphan in sorted(orphans):
        print(orphan)

if __name__ == "__main__":
    audit()
