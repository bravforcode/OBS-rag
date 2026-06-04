#!/usr/bin/env python3
"""
Obsidian Performance Optimizer — Second Brain
Excludes heavy folders from Obsidian indexing while keeping them accessible.

Usage: python optimize-obsidian.py
"""

import json
import os
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
OBSIDIAN_DIR = VAULT_ROOT / ".obsidian"

# Folders to EXCLUDE from Obsidian indexing
# These are still accessible via file system and agents, just not indexed
EXCLUDED_FOLDERS = [
    "brain/skills-universal",      # 1,390+ skill files
    "brain/skills-universal-master",  # duplicate
    "brain/github-skills",         # external repos
    "brain/skills-archive",        # archived skills
    "skills",                      # 165MB external repos
    "Backups",                     # backup files
    ".git",                        # git data
    ".ai/scripts",                 # automation scripts
    ".claude",                     # claude config
    ".github",                     # github config
    ".antigravity",                # ide config
    ".windsurf",                   # ide config
    ".smart-env",                  # search index
    "My-Brain-Is-Full-Crew",       # external project
    "01-projects/*/delta",         # session logs
    "01-projects/*/sessions",      # session data
]


def create_performance_config():
    """Create Obsidian performance config."""
    # 1. Update app.json with exclusions
    app_config_path = OBSIDIAN_DIR / "app.json"
    with open(app_config_path, 'r', encoding='utf-8') as f:
        app_config = json.load(f)

    # Add exclusion list
    app_config["excludedFolders"] = EXCLUDED_FOLDERS

    with open(app_config_path, 'w', encoding='utf-8') as f:
        json.dump(app_config, f, indent=2)
    print("Updated app.json with excluded folders")


def optimize_graph():
    """Disable heavy graph features."""
    graph_path = OBSIDIAN_DIR / "graph.json"
    if graph_path.exists():
        with open(graph_path, 'r', encoding='utf-8') as f:
            graph_config = json.load(f)

        # Reduce graph complexity
        graph_config["collapse-filter"] = True
        graph_config["hideUnresolved"] = True
        graph_config["nodeSizeMultiplier"] = 0.8
        graph_config["linkDistance"] = 200
        graph_config["repelStrength"] = 5

        with open(graph_path, 'w', encoding='utf-8') as f:
            json.dump(graph_config, f, indent=2)
        print("Optimized graph settings")


def reduce_plugins():
    """Keep only essential plugins."""
    plugins_path = OBSIDIAN_DIR / "community-plugins.json"
    # Keep minimal essential plugins
    essential = [
        "dataview",
        "obsidian-git",
        "templater-obsidian",
    ]
    with open(plugins_path, 'w', encoding='utf-8') as f:
        json.dump(essential, f, indent=2)
    print(f"Reduced plugins to {len(essential)} essentials")


def create_exclusion_guide():
    """Create a guide for manual exclusion in Obsidian."""
    guide = """# Obsidian Performance Fix

## Problem
Vault has 7,500+ notes + 165MB of external skill repos.
Obsidian indexes ALL files, causing lag.

## Solution: Exclude Heavy Folders

### Automatic (already applied)
The `.obsidian/app.json` now excludes these folders from indexing:
- `brain/skills-universal/` (1,390 files)
- `brain/skills-universal-master/` (1,390 files)
- `brain/github-skills/`
- `brain/skills-archive/`
- `skills/` (165MB)
- `Backups/`
- `.git/`
- `.ai/scripts/`
- `.claude/`
- `.github/`

### Manual (if still slow)
1. Open Obsidian Settings → Files & Links
2. Add to "Excluded folders":
   - `brain/skills-universal`
   - `skills`
   - `Backups`
3. Disable Graph View when not needed (Ctrl+G to toggle)

### Files Still Accessible
These files are NOT deleted — they're just not indexed by Obsidian.
- Agents can still read them via file system
- CLI tools can still access them
- Manual file access works fine

### If You Need to Search Excluded Folders
Use the file system directly:
```bash
ls brain/skills-universal/
find skills/ -name "*.md"
```
"""
    guide_path = VAULT_ROOT / "meta" / "health" / "performance-fix.md"
    guide_path.parent.mkdir(parents=True, exist_ok=True)
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide)
    print("Created performance fix guide")


if __name__ == "__main__":
    print("=" * 60)
    print("OBSIDIAN PERFORMANCE OPTIMIZER")
    print("=" * 60)

    create_performance_config()
    optimize_graph()
    reduce_plugins()
    create_exclusion_guide()

    print("\n" + "=" * 60)
    print("DONE! Restart Obsidian for changes to take effect.")
    print("=" * 60)
