#!/usr/bin/env python3
"""
Config Sync Script — Second Brain
Syncs vault config from .ai/ authority to all tool configs.

Usage: python config-sync.py [--dry-run]
"""

import json
import os
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
AI_DIR = VAULT_ROOT / ".ai"
CONFIG_FILE = AI_DIR / "vault-config.json"


def load_config():
    """Load the authoritative vault config."""
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def sync_claude_config(config):
    """Sync CLAUDE.md with config authority info."""
    claude_path = VAULT_ROOT / "CLAUDE.md"
    if not claude_path.exists():
        return False

    content = claude_path.read_text(encoding='utf-8')

    # Add config authority reference if not present
    if "vault-config.json" not in content:
        # Add after the routing section
        authority_note = f"""
## Config Authority

All vault configuration is managed from `.ai/vault-config.json`.
This file is the single source of truth for:
- Agent definitions and routing
- Skill registry and loading
- MCP server configuration
- Model routing and budget limits
- Backup and health check settings

To update any vault setting, modify `.ai/vault-config.json` first,
then run `.ai/scripts/config-sync.py` to propagate changes.
"""
        # Insert before the last section
        lines = content.split('\n')
        insert_pos = len(lines) - 1
        for i, line in enumerate(lines):
            if line.startswith('## Hard Constraints'):
                insert_pos = i
                break
        lines.insert(insert_pos, authority_note)
        claude_path.write_text('\n'.join(lines), encoding='utf-8')
        return True
    return False


def sync_copilot_config(config):
    """Sync .github/copilot-instructions.md with config authority."""
    copilot_path = VAULT_ROOT / ".github" / "copilot-instructions.md"
    if not copilot_path.exists():
        return False

    content = copilot_path.read_text(encoding='utf-8')

    if "vault-config.json" not in content:
        authority_note = f"""

## Config Authority

All vault configuration is managed from `.ai/vault-config.json`.
Skills, agents, and routing are defined there. This file references
the same config for Copilot/Codex compatibility.
"""
        content += authority_note
        copilot_path.write_text(content, encoding='utf-8')
        return True
    return False


def sync_mcp_config(config):
    """Ensure .mcp.json matches vault config."""
    mcp_path = VAULT_ROOT / ".mcp.json"
    mcp_servers = config.get("mcp", {}).get("servers", [])

    current = {}
    if mcp_path.exists():
        with open(mcp_path, 'r', encoding='utf-8') as f:
            current = json.load(f)

    # Build expected config
    expected = {"mcpServers": {}}
    for server in mcp_servers:
        if server == "Gmail":
            expected["mcpServers"]["Gmail"] = {
                "type": "http",
                "url": "https://gmail.mcp.claude.com/mcp"
            }
        elif server == "Google Calendar":
            expected["mcpServers"]["Google Calendar"] = {
                "type": "http",
                "url": "https://gcal.mcp.claude.com/mcp"
            }

    if current != expected:
        with open(mcp_path, 'w', encoding='utf-8') as f:
            json.dump(expected, f, indent=2)
        return True
    return False


def sync_model_router(config):
    """Sync model-router.json from vault config."""
    router_path = AI_DIR / "model-router.json"
    router_config = config.get("model_router", {})

    expected = {"routing_rules": []}
    for task_type, settings in router_config.items():
        expected["routing_rules"].append({
            "task_type": task_type,
            "model": settings["model"],
            "provider": settings["provider"]
        })

    current = {}
    if router_path.exists():
        with open(router_path, 'r', encoding='utf-8') as f:
            current = json.load(f)

    if current != expected:
        with open(router_path, 'w', encoding='utf-8') as f:
            json.dump(expected, f, indent=4)
        return True
    return False


def sync_budget_config(config):
    """Sync budget-config.json from vault config."""
    budget_path = AI_DIR / "budget-config.json"
    budget = config.get("budget", {})

    expected = {
        "token_limits": {
            "daily_soft_limit": budget.get("daily_soft_limit", 500000),
            "daily_hard_limit": budget.get("daily_hard_limit", 1000000),
            "per_task_limit": budget.get("per_task_limit", 50000)
        },
        "actions": {
            "on_soft_limit": "warn",
            "on_hard_limit": "block",
            "on_high_cost_task": "require_confirmation"
        },
        "currency": budget.get("currency", "USD")
    }

    current = {}
    if budget_path.exists():
        with open(budget_path, 'r', encoding='utf-8') as f:
            current = json.load(f)

    if current != expected:
        with open(budget_path, 'w', encoding='utf-8') as f:
            json.dump(expected, f, indent=2)
        return True
    return False


def sync_all(dry_run=True):
    """Sync all configs from authority."""
    config = load_config()
    results = {}

    syncs = [
        ("CLAUDE.md", sync_claude_config),
        ("copilot-instructions.md", sync_copilot_config),
        (".mcp.json", sync_mcp_config),
        ("model-router.json", sync_model_router),
        ("budget-config.json", sync_budget_config),
    ]

    for name, sync_func in syncs:
        if dry_run:
            # Just check if sync would be needed
            results[name] = "would check"
        else:
            try:
                changed = sync_func(config)
                results[name] = "updated" if changed else "already sync"
            except Exception as e:
                results[name] = f"error: {e}"

    return results


if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv

    print(f"{'DRY RUN' if dry_run else 'EXECUTING'}: Config Sync")
    print("=" * 60)

    results = sync_all(dry_run)

    for name, status in results.items():
        print(f"  {name}: {status}")

    if dry_run:
        print(f"\nRun without --dry-run to execute.")
    else:
        print(f"\nConfig sync complete!")
        print(f"Authority: .ai/vault-config.json")
