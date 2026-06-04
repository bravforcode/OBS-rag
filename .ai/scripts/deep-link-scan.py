#!/usr/bin/env python3
"""
Deep Link Scanner — Second Brain
Finds broken links, orphan notes, and link health metrics.

Usage: python deep-link-scan.py
"""

import os
import re
from pathlib import Path
from collections import Counter, defaultdict

VAULT_ROOT = Path(__file__).parent.parent.parent
REPORT_PATH = VAULT_ROOT / "Meta" / "health" / "link-scan-report.md"


def scan_vault():
    """Scan all markdown files for links and notes."""
    all_notes = {}  # name -> relative path
    all_links = []  # (source_file, link_target, line_number)
    note_contents = {}  # path -> content

    for root, dirs, files in os.walk(VAULT_ROOT):
        dirs[:] = [d for d in dirs if d not in {
            '.git', 'node_modules', '__pycache__', '.smart-env', 'Backups',
            '.obsidian', '.obsidian-mobile', '.antigravity'
        }]
        for f in files:
            if not f.endswith('.md'):
                continue
            filepath = Path(root) / f
            rel_path = filepath.relative_to(VAULT_ROOT)
            note_name = f[:-3]  # Remove .md

            # Register note
            all_notes[note_name] = str(rel_path)
            # Also register with path-based key
            path_key = str(rel_path).replace('\\', '/').replace('.md', '')
            all_notes[path_key] = str(rel_path)

            # Read and parse links
            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                note_contents[str(rel_path)] = content

                # Find wiki-links [[target]] or [[target|display]]
                link_pattern = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+)?\]\]')
                for i, line in enumerate(content.split('\n'), 1):
                    for match in link_pattern.finditer(line):
                        target = match.group(1).strip()
                        all_links.append((str(rel_path), target, i))
            except Exception:
                pass

    return all_notes, all_links, note_contents


def find_broken_links(all_notes, all_links):
    """Find links that don't resolve to any note."""
    broken = []
    for source, target, line in all_links:
        # Skip external links
        if target.startswith('http') or target.startswith('mailto'):
            continue

        # Clean target (remove .md extension if present)
        clean_target = target.replace('.md', '').replace('\\', '/')

        # Check various resolution strategies
        resolved = False

        # 1. Direct name match
        if clean_target in all_notes:
            resolved = True

        # 2. Path-based match
        if not resolved:
            for key in all_notes:
                if clean_target.lower() == key.lower():
                    resolved = True
                    break

        # 3. Filename match (last component)
        if not resolved:
            filename = clean_target.split('/')[-1]
            if filename in all_notes:
                resolved = True

        # 4. Partial path match
        if not resolved:
            for key in all_notes:
                if clean_target.lower() in key.lower() or key.lower() in clean_target.lower():
                    resolved = True
                    break

        if not resolved:
            broken.append((source, target, line))

    return broken


def find_orphan_notes(all_notes, all_links):
    """Find notes with no incoming links."""
    # Build set of all linked targets
    linked_targets = set()
    for _, target, _ in all_links:
        clean = target.replace('.md', '').replace('\\', '/').split('/')[-1]
        linked_targets.add(clean.lower())

    orphans = []
    for name, path in all_notes.items():
        # Skip index files, MOCs, and system files
        if any(skip in name.lower() for skip in ['index', 'moc', 'readme', 'changelog', 'architecture']):
            continue
        if name.lower() not in linked_targets:
            orphans.append((name, path))

    return orphans


def analyze_link_density(all_notes, all_links):
    """Analyze link density per note."""
    incoming = Counter()
    outgoing = Counter()

    for source, target, _ in all_links:
        clean_target = target.split('/')[-1].replace('.md', '').lower()
        outgoing[source] += 1
        incoming[clean_target] += 1

    # Find most linked notes
    most_linked = incoming.most_common(20)

    # Find notes with most outgoing links
    most_outgoing = outgoing.most_common(20)

    return most_linked, most_outgoing


def generate_report(all_notes, all_links, broken, orphans, most_linked, most_outgoing):
    """Generate the link scan report."""
    total_notes = len(all_notes)
    total_links = len(all_links)
    broken_count = len(broken)
    orphan_count = len(orphans)

    report = f"""---
type: health-report
generated: '2026-06-04'
---

# Deep Link Scan Report

Generated: 2026-06-04

## Summary

| Metric | Value |
|--------|-------|
| Total notes | {total_notes} |
| Total wiki-links | {total_links} |
| Broken links | {broken_count} |
| Orphan notes | {orphan_count} |
| Link density | {total_links / max(total_notes, 1):.1f} links/note |

## Health Rating

"""
    if broken_count == 0 and orphan_count < 10:
        report += "**EXCELLENT** — Vault is well-connected and healthy.\n\n"
    elif broken_count < 10 and orphan_count < 50:
        report += "**GOOD** — Minor issues to address.\n\n"
    elif broken_count < 50:
        report += "**FAIR** — Some cleanup recommended.\n\n"
    else:
        report += "**NEEDS ATTENTION** — Significant link issues found.\n\n"

    # Broken links
    report += "## Broken Links\n\n"
    if broken:
        report += "| Source | Target | Line |\n|--------|--------|------|\n"
        for source, target, line in broken[:50]:
            report += f"| `{source}` | `[[{target}]]` | {line} |\n"
        if len(broken) > 50:
            report += f"\n*... and {len(broken) - 50} more broken links*\n"
    else:
        report += "No broken links found! ✓\n"
    report += "\n"

    # Orphan notes
    report += "## Orphan Notes (No Incoming Links)\n\n"
    if orphans:
        report += "| Note | Path |\n|------|------|\n"
        for name, path in orphans[:30]:
            report += f"| `{name}` | `{path}` |\n"
        if len(orphans) > 30:
            report += f"\n*... and {len(orphans) - 30} more orphan notes*\n"
    else:
        report += "No orphan notes found! ✓\n"
    report += "\n"

    # Most linked notes
    report += "## Most Connected Notes (Incoming Links)\n\n"
    report += "| Note | Incoming Links |\n|------|----------------|\n"
    for name, count in most_linked:
        report += f"| `{name}` | {count} |\n"
    report += "\n"

    # Most outgoing links
    report += "## Notes With Most Outgoing Links\n\n"
    report += "| Note | Outgoing Links |\n|------|----------------|\n"
    for name, count in most_outgoing[:15]:
        report += f"| `{name}` | {count} |\n"
    report += "\n"

    # Recommendations
    report += "## Recommendations\n\n"
    if broken_count > 0:
        report += f"1. **Fix {broken_count} broken links** — Review and update or remove dead links\n"
    if orphan_count > 20:
        report += f"2. **Link {orphan_count} orphan notes** — Add incoming links to connect them to the knowledge graph\n"
    if total_links / max(total_notes, 1) < 2:
        report += "3. **Increase link density** — Aim for 3+ links per note\n"
    if broken_count == 0 and orphan_count < 10:
        report += "1. **Maintain current health** — Vault is in excellent shape\n"
    report += "\n"

    report += "---\n*Report generated by deep-link-scan.py*\n"

    return report


if __name__ == "__main__":
    print("Scanning vault...")
    all_notes, all_links, note_contents = scan_vault()
    print(f"Found {len(all_notes)} notes, {len(all_links)} links")

    print("Finding broken links...")
    broken = find_broken_links(all_notes, all_links)
    print(f"Found {len(broken)} broken links")

    print("Finding orphan notes...")
    orphans = find_orphan_notes(all_notes, all_links)
    print(f"Found {len(orphans)} orphan notes")

    print("Analyzing link density...")
    most_linked, most_outgoing = analyze_link_density(all_notes, all_links)

    print("Generating report...")
    report = generate_report(all_notes, all_links, broken, orphans, most_linked, most_outgoing)

    # Save report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding='utf-8')
    print(f"Report saved to: {REPORT_PATH}")

    # Print summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total notes: {len(all_notes)}")
    print(f"Total links: {len(all_links)}")
    print(f"Broken links: {len(broken)}")
    print(f"Orphan notes: {len(orphans)}")
    print(f"Link density: {len(all_links) / max(len(all_notes), 1):.1f} links/note")
    print(f"{'='*60}")
