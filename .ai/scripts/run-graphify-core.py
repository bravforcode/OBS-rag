#!/usr/bin/env python3
"""
Run Graphify on Core Vault Files Only
Excludes heavy external repos for faster processing.

Usage: python run-graphify-core.py
"""

import os
import sys
import json
import shutil
import tempfile
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
GRAPHIFY_OUT = VAULT_ROOT / "graphify-out"

# Folders to exclude from graphify
EXCLUDE = {
    "brain", "skills", "Backups", ".git", ".smart-env",
    "node_modules", "__pycache__", ".ai/scripts",
    "graphify-out", "My-Brain-Is-Full-Crew",
    ".obsidian", ".obsidian-mobile",
    ".claude", ".github", ".antigravity", ".windsurf",
}


def create_filtered_copy():
    """Create a temporary copy with only core files."""
    tmp_dir = Path(tempfile.mkdtemp(prefix="graphify_"))
    print(f"Creating filtered copy in {tmp_dir}...")

    for item in VAULT_ROOT.iterdir():
        if item.name.startswith(".") or item.name in EXCLUDE:
            continue
        if item.is_dir():
            shutil.copytree(item, tmp_dir / item.name, ignore=shutil.ignore_patterns(*EXCLUDE))
        else:
            shutil.copy2(item, tmp_dir / item.name)

    file_count = sum(1 for _ in tmp_dir.rglob("*") if _.is_file())
    print(f"Filtered copy: {file_count} files")
    return tmp_dir


def run_graphify(tmp_dir):
    """Run graphify on filtered copy."""
    os.chdir(tmp_dir)
    GRAPHIFY_OUT.mkdir(exist_ok=True)

    print("\n[1/3] Detecting...")
    os.system("graphify . 2>&1")

    print("\n[2/3] Copying results back...")
    if (tmp_dir / "graphify-out").exists():
        shutil.copytree(tmp_dir / "graphify-out", GRAPHIFY_OUT, dirs_exist_ok=True)
        print(f"Results copied to {GRAPHIFY_OUT}")

    print("\n[3/3] Cleaning up...")
    shutil.rmtree(tmp_dir, ignore_errors=True)
    print("Done!")


if __name__ == "__main__":
    tmp_dir = create_filtered_copy()
    run_graphify(tmp_dir)
