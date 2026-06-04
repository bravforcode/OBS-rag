#!/usr/bin/env python3
"""
Fix Broken Links — Second Brain
Auto-fixes genuinely broken links (not templates or hidden configs).

Usage: python fix-broken-links.py [--dry-run]
"""

import os
import re
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent

# Links to remove (reference deleted brain/auto-systems/)
REMOVE_PATTERNS = [
    r'\[\[brain/auto-systems/auto_linker\]\]',
    r'\[\[brain/auto-systems/auto_classifier\]\]',
    r'\[\[brain/auto-systems/auto_tagger\]\]',
    r'\[\[brain/auto-systems/vault_optimizer\]\]',
    r'\[\[auto_linker\]\]',
    r'\[\[auto_classifier\]\]',
    r'\[\[auto_tagger\]\]',
    r'\[\[vault_optimizer\]\]',
]

# Links to fix (old -> new)
FIX_MAP = {
    "[[WikiLinks]]": "[[Obsidian Markdown|Wiki-Links]]",
    "[[wikilinks]]": "[[Obsidian Markdown|wiki-links]]",
    "[[00-Inbox]]": "[[00-inbox/Index|00-Inbox]]",
    "[[Marco]]": "[[example contact]]",
    "[[Marco Rossi]]": "[[example contact]]",
    "[[Monthly Report]]": "[[example report]]",
    "[[Weekly Report]]": "[[example report]]",
    "[[Token Usage Report]]": "[[Intelligence/Token_Optimization_Strategy|Token Optimization]]",
    "[[links]]": "[[linking guide]]",
    "[[Paper]]": "[[research paper]]",
    "[[Model card]]": "[[model documentation]]",
    "[[Colab example]]": "[[colab notebook]]",
    "[[MyBase.base]]": "[[example database]]",
    "[[MyBase.base#View Name]]": "[[example database]]",
    "[[หน้าอื่น]]": "[[related notes]]",
}


def fix_broken_links(dry_run=True):
    """Fix broken links in vault files."""
    changes = []

    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if d not in {
            '.git', 'node_modules', '__pycache__', '.smart-env', 'Backups'
        }]
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = Path(root) / f
            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                new_content = content

                # Remove dead auto-system links
                for pattern in REMOVE_PATTERNS:
                    new_content = re.sub(pattern, '', new_content)

                # Fix known broken links
                for old, new in FIX_MAP.items():
                    new_content = new_content.replace(old, new)

                # Clean up empty lines left by removal
                new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

                if new_content != content:
                    changes.append(str(filepath.relative_to(VAULT_ROOT)))
                    if not dry_run:
                        filepath.write_text(new_content, encoding='utf-8')
            except Exception as e:
                changes.append(f"ERROR: {filepath} - {e}")

    return changes


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv

    print(f"{'DRY RUN' if dry_run else 'EXECUTING'}: Fix Broken Links")
    print("=" * 60)

    changes = fix_broken_links(dry_run)

    print(f"\nFiles modified: {len(changes)}")
    for c in changes:
        print(f"  {c}")

    if dry_run:
        print(f"\nRun without --dry-run to execute.")
    else:
        print(f"\nDone! {len(changes)} files fixed.")
