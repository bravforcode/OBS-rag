import os
import re
import sys
from pathlib import Path

def check_links():
    # Execute from the root of the repository
    repo_root = Path(".").resolve()
    
    # Find all markdown files, ignoring .github and other hidden directories if needed
    md_files = [f for f in repo_root.rglob("*.md") if not str(f.relative_to(repo_root)).startswith('.')]
    
    # Build a set of all valid markdown file stems (filenames without extension)
    # Also keep track of full paths to detect orphans
    valid_stems = {f.stem for f in md_files}
    
    # Regex to find Obsidian links [[link]] or [[link|alias]]
    link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
    
    broken_links = []
    referenced_stems = set()
    
    for file_path in md_files:
        try:
            content = file_path.read_text(encoding='utf-8')
            links = link_pattern.findall(content)
            for link in links:
                # Obsidian links can sometimes have # for headings, remove it for file check
                clean_link = link.split('#')[0].strip()
                if clean_link:
                    referenced_stems.add(clean_link)
                    if clean_link not in valid_stems:
                        broken_links.append((file_path.relative_to(repo_root), clean_link))
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Check for orphans (files not referenced by any other file, ignoring typical entry points like README)
    # We might not want to fail CI for orphans, just warn.
    orphans = []
    for f in md_files:
        if f.stem not in referenced_stems and f.stem.lower() not in ('readme', 'index', 'home'):
            orphans.append(f.relative_to(repo_root))

    if orphans:
        print("Warning: Found potentially orphaned files:")
        for orphan in orphans:
            print(f"- '{orphan}'")
        print()

    if broken_links:
        print("Error: Found broken links:")
        for file_path, link in broken_links:
            print(f"- In '{file_path}': Broken link to '[[{link}]]'")
        sys.exit(1)
    else:
        print("Success: No broken links found. Graph is fully connected!")

if __name__ == "__main__":
    check_links()