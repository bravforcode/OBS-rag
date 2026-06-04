import json
import os
import shutil
import argparse

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "bridge-config.json")

def sync(dry_run=False):
    if not os.path.exists(CONFIG_PATH):
        print(f"Config not found at {CONFIG_PATH}")
        return

    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)

    for pair in config.get("sync_pairs", []):
        obsidian_path = pair.get("obsidian_path")
        codebase_path = pair.get("codebase_path")

        if not obsidian_path or not codebase_path:
            continue

        print(f"Syncing {obsidian_path} <-> {codebase_path}")
        
        # Implementation could be complex (rsync style), 
        # but for now we'll just check existence and maybe list differences.
        # A simple one-way sync from codebase to obsidian for docs might be safer.
        
        # Let's say we sync .md files from codebase/docs to obsidian project folder
        code_docs = os.path.join(codebase_path, "docs")
        if os.path.exists(code_docs):
            for item in os.listdir(code_docs):
                if item.endswith(".md"):
                    src = os.path.join(code_docs, item)
                    dst = os.path.join(obsidian_path, item)
                    if dry_run:
                        print(f"[DRY RUN] Would copy {src} to {dst}")
                    else:
                        shutil.copy2(src, dst)
                        print(f"Synced: {item}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_argument()
    sync(dry_run=args.dry_run)
