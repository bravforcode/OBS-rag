#!/usr/bin/env python3
"""
Vault Health Check — Second Brain
Runs comprehensive diagnostics on the vault.

Usage: python vault-health-check.py
"""

import os
import re
from pathlib import Path
from collections import Counter

VAULT_ROOT = Path(__file__).parent.parent.parent


def count_files():
    """Count files by type."""
    counts = Counter()
    total = 0
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Skip hidden and system dirs
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'node_modules', '__pycache__', 'Backups'}]
        for f in files:
            ext = Path(f).suffix.lower()
            counts[ext] += 1
            total += 1
    return total, counts


def check_broken_links():
    """Find wiki links that don't resolve."""
    broken = []
    all_notes = set()
    
    # Collect all note names
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                all_notes.add(f[:-3])  # Remove .md
    
    # Check links
    link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = Path(root) / f
            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                for match in link_pattern.finditer(content):
                    link_target = match.group(1).strip()
                    # Simple check: does any note contain this text?
                    if link_target not in all_notes and not any(link_target in note for note in all_notes):
                        broken.append((str(filepath), link_target))
            except Exception:
                pass
    return broken


def check_large_files(threshold_kb=100):
    """Find files larger than threshold."""
    large = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            filepath = Path(root) / f
            size_kb = filepath.stat().st_size / 1024
            if size_kb > threshold_kb:
                large.append((str(filepath), round(size_kb, 1)))
    return sorted(large, key=lambda x: -x[1])


def check_empty_folders():
    """Find empty directories."""
    empty = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for d in dirs:
            dirpath = Path(root) / d
            if not any(dirpath.iterdir()):
                empty.append(str(dirpath))
    return empty


def check_frontmatter():
    """Check if files have proper frontmatter."""
    no_frontmatter = []
    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = Path(root) / f
            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                if content.strip() and not content.startswith('---'):
                    no_frontmatter.append(str(filepath))
            except Exception:
                pass
    return no_frontmatter[:50]  # Limit output


def run_health_check():
    """Run all health checks."""
    print("=" * 60)
    print("VAULT HEALTH CHECK — Second Brain")
    print("=" * 60)
    
    # File counts
    total, counts = count_files()
    print(f"\nFILE COUNTS")
    print(f"   Total files: {total}")
    for ext, count in counts.most_common(10):
        print(f"   {ext or '(no ext)'}: {count}")
    
    # Broken links
    broken = check_broken_links()
    print(f"\nBROKEN LINKS: {len(broken)}")
    for filepath, target in broken[:10]:
        print(f"   {filepath} -> [[{target}]]")
    if len(broken) > 10:
        print(f"   ... and {len(broken) - 10} more")
    
    # Large files
    large = check_large_files()
    print(f"\nLARGE FILES (>100KB): {len(large)}")
    for filepath, size in large[:10]:
        print(f"   {size}KB — {filepath}")
    
    # Empty folders
    empty = check_empty_folders()
    print(f"\nEMPTY FOLDERS: {len(empty)}")
    for folder in empty:
        print(f"   {folder}")
    
    # Frontmatter
    no_fm = check_frontmatter()
    print(f"\nFILES WITHOUT FRONTMATTER: {len(no_fm)}")
    
    # Summary
    print(f"\n" + "=" * 60)
    issues = len(broken) + len(large) + len(empty) + len(no_fm)
    if issues == 0:
        print("VAULT HEALTH: EXCELLENT")
    elif issues < 10:
        print("VAULT HEALTH: GOOD (minor issues)")
    elif issues < 50:
        print("VAULT HEALTH: FAIR (needs attention)")
    else:
        print("VAULT HEALTH: POOR (significant issues)")
    print(f"   Total issues found: {issues}")
    print("=" * 60)


if __name__ == "__main__":
    run_health_check()
