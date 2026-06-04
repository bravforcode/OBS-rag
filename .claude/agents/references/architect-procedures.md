# Architect — Detailed Procedures & Templates

Full procedures for the Architect agent. The main `architect.md` is the lean system prompt; this file is loaded only when structural work is being done.

## Area Scaffolding Procedure (7 steps)

**Most important structural operation.** Every new area follows this exact procedure.

### Step 1: Folder Structure

Create area under `02-areas/` with sub-folders based on user's description. Use Phase 2a follow-up answers to decide contents.

### Step 2: Area Index (`_index.md`)

Every area gets `_index.md` — its home page with description, active project links, key resources. Template:

```markdown
---
type: area
date: "{{today}}"
tags: [area, {{area-tag}}]
---

# {{Area Name}}

## Purpose
{{Brief description of why this area exists}}

## Active Projects
{{Links to projects in this area — empty at creation}}

## Sub-Areas
{{Links to sub-folders if any}}

## Key Resources
{{Links to important reference notes}}

## MOC
→ [[{{Area Name}}]]
```

### Step 3: Area MOC

Create `MOC/{{Area Name}}.md`:

```markdown
---
type: moc
date: "{{today}}"
tags: [moc, {{area-tag}}]
---

# {{Area Name}} — Map of Content

## Overview
{{Description of what this area covers}}

## Structure
{{List of sub-folders and their purpose}}

## Key Notes
{{Will be populated as notes are added}}

## Active Projects
{{Links to active projects in this area}}

## Related MOCs
- [[Index|Master Index]]
{{Links to related area MOCs}}
```

### Step 4: Update Master MOC

Add link to new area in `MOC/Index.md`.

### Step 5: Area-Specific Templates

If area needs specialized templates (e.g., Finance needs Budget Entry, Investment), create in `Templates/`.

### Step 6: Update `Meta/vault-structure.md`

Document the new area, sub-folders, purpose.

### Step 7: Update `Meta/tag-taxonomy.md`

Add area-specific tags (e.g., `#area/finance`, `#budget`, `#investment`).

## Folder Management

New project/area/topic:

1. **Evaluate** — does it warrant a new folder? (Rule: 3+ notes expected)
2. **If new Area** — run full Area Scaffolding (7 steps)
3. **If new sub-folder within existing area** — create folder, update `_index.md` and MOC
4. **If new project** — create in `01-projects/` or relevant area, update area MOC
5. **Update `Meta/vault-structure.md`**
6. **Inform other agents** via structure docs + `### Suggested next agent` in output

When user requests new folder, always confirm proposed location + explain reasoning.

## Tag Taxonomy

Maintain in `Meta/tag-taxonomy.md`:

```markdown
# Tag Taxonomy

## Content Types
#meeting #idea #task #note #reference #person #project #area #moc #report #daily

## Status
#inbox #active #on-hold #completed #archived

## Priority
#urgent #high #medium #low

## Topics
{{Organized by domain — add new tags as they emerge}}

## Rules
- All tags lowercase and hyphenated (e.g., #machine-learning, not #MachineLearning)
- No duplicate semantic tags (don't use both #ml and #machine-learning — pick one)
- New tags must be added here before use in notes
- Hierarchical tags use slashes: #project/alpha, #area/marketing
```

## Naming Conventions

Maintain `Meta/naming-conventions.md`:

```markdown
# Naming Conventions

## Files
Pattern: `YYYY-MM-DD — {{Type}} — {{Short Title}}.md`
- Date first for chronological sorting
- Type matches content type: Meeting, Idea, Task, Note, Reference, Call, Voice Note
- Title descriptive, max 50 characters, Title Case
- Separator em dash with spaces: ` — `

Examples:
- `2026-03-21 — Meeting — Q1 Review With Marketing.md`
- `2026-03-21 — Idea — Automated Email Triage.md`
- `2026-03-21 — Note — Obsidian Plugin Research.md`

## Folders
- Top-level: numbered prefix `00-` through `07-`
- Subfolders: plain names, Title Case
- Year/month for temporal: `2026/03/`

## Tags
- Always lowercase, hyphenated
- Hierarchical via slash: #project/alpha, #area/marketing

## People
- Full name, Title Case: `John Smith.md`
- Alias in frontmatter for nicknames

## Daily Notes
- Pattern: `YYYY-MM-DD.md`
- Location: `07-daily/`

## Templates
- Plain name, Title Case: `Meeting.md`, `Daily Note.md`
- Location: `Templates/`
```

## Vault Evolution

Vault is a living organism. Evolve continuously. Don't wait for user to ask.

**Weekly Defragmentation** covers all systematically. Between defrags, act on structural gaps as encountered.

## Profile Updates

User may ask to update profile at any time. Triggers:
- "Update my profile"
- "I changed jobs"
- "I want to add Spanish as a language"

Read `Meta/user-profile.md`, make changes, increment `profile-version`, save. If change affects other files (new life area requires folder structure), make those too.

## Custom Agent Creation

Agent creation: `/create-agent` skill. Agent editing, removal, listing: `/manage-agent` skill. Dispatcher routes these triggers directly.
