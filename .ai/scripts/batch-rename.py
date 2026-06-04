#!/usr/bin/env python3
"""
Batch Rename Script — Second Brain
Renames files to kebab-case and removes emoji prefixes.

Usage: python batch-rename.py [--dry-run]
"""

import os
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent

# Files to rename (old -> new) at root level
ROOT_RENAMES = {
    "📊 SYSTEM-STATUS.md": "system-status.md",
    "🔗 CONNECTION-MAP.md": "connection-map.md",
    "🧭 START-HERE.md": "start-here.md",
    "Atlas.md": "atlas.md",
    "Dashboard.md": "dashboard.md",
    "Welcome.md": "welcome.md",
    "style-guide.md": "style-guide.md",  # already fine
}

# Files to KEEP as-is (convention)
KEEP_AS_IS = {
    "CLAUDE.md", "README.md", "MASTER_AI_RULES.md",
    "ARCHITECTURE.md", "CHANGELOG.md", "CLAUDE.md.bak",
}

# Folders to rename (old -> new)
FOLDER_RENAMES = {
    "01-Projects": "01-projects",
    "02-Areas": "02-areas",
    "03-Resources": "03-resources",
    "04-Archive": "04-archive",
    "05-People": "05-people",
    "06-Meetings": "06-meetings",
    "07-Daily": "07-daily",
    "00-Meta": "00-meta",
    "CRM": "crm",
    "Excalidraw": "excalidraw",
    "Intelligence": "intelligence",
    "Journal": "journal",
    "Knowledge": "knowledge",
    "Lessons": "lessons",
    "Meta": "meta",
    "MOC": "moc",
    "My-Brain-Is-Full-Crew": "my-brain-is-full-crew",
    "Operations": "operations",
    "Second Brain": "second-brain",
    "System": "system",
    "Templates": "templates",
    "wiki": "wiki",
}

# Wiki-link replacements (old path -> new path)
LINK_REPLACEMENTS = {
    "01-Projects/": "01-projects/",
    "02-Areas/": "02-areas/",
    "03-Resources/": "03-resources/",
    "04-Archive/": "04-archive/",
    "05-People/": "05-people/",
    "06-Meetings/": "06-meetings/",
    "07-Daily/": "07-daily/",
    "00-Meta/": "00-meta/",
    "/CRM/": "/crm/",
    "/Excalidraw/": "/excalidraw/",
    "/Intelligence/": "/intelligence/",
    "/Journal/": "/journal/",
    "/Knowledge/": "/knowledge/",
    "/Lessons/": "/lessons/",
    "/Meta/": "/meta/",
    "/MOC/": "/moc/",
    "/Operations/": "/operations/",
    "/System/": "/system/",
    "/Templates/": "/templates/",
    "/wiki/": "/wiki/",
    "System/AI/": "system/ai/",
}


def pascal_to_kebab(name):
    """Convert PascalCase to kebab-case."""
    # Insert hyphens before uppercase letters
    s1 = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', name)
    s2 = re.sub(r'([a-z\d])([A-Z])', r'\1-\2', s1)
    return s2.lower()


def remove_emoji(name):
    """Remove emoji characters from filename."""
    # Remove common emoji ranges
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"  # dingbats
        "\U000024C2-\U0001F251"  # enclosed characters
        "\U0001f926-\U0001f937"  # more emojis
        "\U00010000-\U0010ffff"  # supplementary
        "\u200d"                 # zero width joiner
        "\u2640-\u2642"          # gender symbols
        "\ufe0f"                 # variation selector
        "\u20e3"                 # combining enclosing keycap
        "]+",
        flags=re.UNICODE
    )
    cleaned = emoji_pattern.sub('', name).strip()
    # Also remove leading question marks
    cleaned = cleaned.lstrip('?').strip()
    return cleaned


def rename_files(dry_run=True):
    """Rename files and folders."""
    changes = []

    # Rename root files
    for old_name, new_name in ROOT_RENAMES.items():
        old_path = VAULT_ROOT / old_name
        new_path = VAULT_ROOT / new_name
        if old_path.exists() and old_name not in KEEP_AS_IS:
            if old_name != new_name:
                changes.append(f"FILE: {old_name} -> {new_name}")
                if not dry_run:
                    old_path.rename(new_path)

    # Rename emoji files anywhere in vault
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if d not in {'.git', 'node_modules', '__pycache__', '.smart-env', 'Backups'}]
        for f in files:
            if f in KEEP_AS_IS or f.endswith(('.json', '.py', '.sh', '.yml', '.yaml', '.vbs', '.ps1')):
                continue
            cleaned = remove_emoji(f)
            if cleaned != f and f.endswith('.md'):
                old_path = Path(root) / f
                new_path = Path(root) / cleaned
                changes.append(f"EMOJI: {f} -> {cleaned}")
                if not dry_run:
                    old_path.rename(new_path)

    # Rename folders
    for old_name, new_name in FOLDER_RENAMES.items():
        if old_name == new_name:
            continue
        old_path = VAULT_ROOT / old_name
        new_path = VAULT_ROOT / new_name
        if old_path.exists() and old_path.is_dir():
            changes.append(f"FOLDER: {old_name} -> {new_name}")
            if not dry_run:
                try:
                    old_path.rename(new_path)
                except OSError as e:
                    changes.append(f"  ERROR: {e}")

    return changes


def update_links(dry_run=True):
    """Update wiki-links in all markdown files."""
    changes = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if d not in {'.git', 'node_modules', '__pycache__', '.smart-env', 'Backups'}]
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = Path(root) / f
            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                new_content = content
                for old_link, new_link in LINK_REPLACEMENTS.items():
                    new_content = new_content.replace(old_link, new_link)
                if new_content != content:
                    changes.append(f"LINKS: {filepath.relative_to(VAULT_ROOT)}")
                    if not dry_run:
                        filepath.write_text(new_content, encoding='utf-8')
            except Exception as e:
                changes.append(f"ERROR: {filepath} - {e}")
    return changes


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv

    print(f"{'DRY RUN' if dry_run else 'EXECUTING'}: Batch Rename")
    print("=" * 60)

    file_changes = rename_files(dry_run)
    link_changes = update_links(dry_run)

    print(f"\nFile/Folder renames: {len(file_changes)}")
    for c in file_changes:
        print(f"  {c}")

    print(f"\nLink updates: {len(link_changes)}")
    for c in link_changes[:20]:
        print(f"  {c}")
    if len(link_changes) > 20:
        print(f"  ... and {len(link_changes) - 20} more")

    if dry_run:
        print(f"\nRun without --dry-run to execute.")
    else:
        print(f"\nDone! {len(file_changes)} renames, {len(link_changes)} link updates.")
