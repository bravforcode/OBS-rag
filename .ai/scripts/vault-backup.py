#!/usr/bin/env python3
"""
Vault Backup Script — Second Brain
Creates timestamped backups of the vault.

Usage: python backup-vault.py [--full | --incremental]
"""

import os
import shutil
import json
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
BACKUP_DIR = VAULT_ROOT / "Backups"
MANIFEST_FILE = BACKUP_DIR / "backup-manifest.json"

# Directories to backup
BACKUP_SOURCES = [
    "00-Inbox", "01-Projects", "02-Areas", "03-Resources",
    "04-Archive", "05-People", "06-Meetings", "07-Daily",
    "MOC", "Meta", "Templates", "System", "Knowledge",
    "Intelligence", "Operations", "CRM", "Journal",
    "CLAUDE.md", "MASTER_AI_RULES.md", "README.md",
    "Dashboard.md", "Atlas.md", ".gitignore",
]

# Directories to skip
SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".smart-env",
    "Backups", ".obsidian", ".obsidian-mobile",
}


def create_backup(incremental=False):
    """Create a timestamped backup of the vault."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_name = f"vault-backup-{timestamp}"
    backup_path = BACKUP_DIR / backup_name

    BACKUP_DIR.mkdir(exist_ok=True)
    backup_path.mkdir(exist_ok=True)

    backed_up = []
    skipped = []

    for source in BACKUP_SOURCES:
        src_path = VAULT_ROOT / source
        if not src_path.exists():
            skipped.append(source)
            continue

        dst_path = backup_path / source
        if src_path.is_dir():
            shutil.copytree(src_path, dst_path, ignore=shutil.ignore_patterns(*SKIP_DIRS))
        else:
            shutil.copy2(src_path, dst_path)
        backed_up.append(source)

    # Save manifest
    manifest = {
        "timestamp": timestamp,
        "backup_name": backup_name,
        "type": "full" if not incremental else "incremental",
        "backed_up": backed_up,
        "skipped": skipped,
        "vault_root": str(VAULT_ROOT),
    }

    manifest_path = backup_path / "backup-manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    # Update global manifest
    history = []
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE) as f:
            history = json.load(f).get("backups", [])
    history.append(manifest)
    with open(MANIFEST_FILE, "w") as f:
        json.dump({"backups": history[-50:]}, f, indent=2)  # Keep last 50

    print(f"Backup created: {backup_path}")
    print(f"Files backed up: {len(backed_up)}")
    print(f"Skipped: {len(skipped)}")
    return backup_path


if __name__ == "__main__":
    import sys
    incremental = "--incremental" in sys.argv
    create_backup(incremental)
