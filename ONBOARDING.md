# ONBOARDING.md

Welcome to the Second Brain. This guide gets you productive in under 10 minutes.

## Step 1: Open the Vault

Open this folder in Obsidian. The vault root is this directory.

## Step 2: Understand the Structure

```
Second Brain/
├── 00-inbox/          ← Dump everything here first
├── 01-projects/       ← Active work with goals
├── 02-areas/          ← Life areas you maintain
├── 03-resources/      ← Reference material
├── 04-archive/        ← Old completed stuff
├── 05-people/         ← Contacts
├── 06-meetings/       ← Meeting notes
├── 07-daily/          ← Daily notes
├── moc/               ← Maps of Content (indexes)
├── meta/              ← Vault governance
├── templates/         ← Note templates
├── system/            ← Identity, constraints, voice
├── knowledge/         ← Playbooks, lessons
├── intelligence/      ← Strategic reports
├── skills/            ← AI skills
├── crm/               ← Contacts
├── journal/           ← Daily/weekly journals
└── operations/        ← Tasks, opportunities
```

## Step 3: Capture Your First Note

1. Press `Ctrl+N` (new note)
2. Use template: `Ctrl+P` → "Templater: Insert template"
3. Choose a template type (Daily Note, Meeting, Idea, etc.)

## Step 4: Connect Your Notes

Use Obsidian `[[wiki-links]]` to connect notes:
- `[[Dashboard]]` — link to dashboard
- `[[01-projects/your-project|Your Project]]` — link with display text
- The more links you create, the more useful the graph view becomes

## Step 5: Use AI Agents

Type these commands in any note:

| Command | What Happens |
|---------|--------------|
| `/plan` | Architect helps structure your vault |
| `/capture` | Scribe captures raw text to inbox |
| `/search` | Seeker finds information |
| `/audit` | Librarian checks vault health |
| `/research` | Researcher does web research |
| `/pulse` | Pulse generates daily digest |

## Step 6: Navigate

- **Dashboard**: Open `Dashboard.md` for overview
- **Graph View**: `Ctrl+G` to see connections
- **Search**: `Ctrl+O` to quick-open any note
- **MOCs**: Start at `moc/MOC-root.md`

## Step 7: Daily Workflow

```
Morning:
  1. Open Dashboard
  2. Check today's tasks
  3. Process inbox items

During Day:
  1. Capture ideas to 00-inbox/
  2. Link new notes to existing ones
  3. Update project notes

Evening:
  1. Run /pulse for daily digest
  2. Review what you learned
  3. Plan tomorrow
```

## Step 8: Weekly Maintenance

```
1. Run /audit — Librarian checks vault health
2. Review orphan notes — add links or archive
3. Update MOCs if new topics emerged
4. Clean inbox — move processed items to proper folders
```

## Getting Help

- Check `Welcome.md` for comprehensive documentation
- See `ARCHITECTURE.md` for system design
- Run `vault-health-check.py` for diagnostics
- Ask an agent: "help me with [topic]"

---

*You're all set. Start capturing and connecting.*
