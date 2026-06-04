# Second Brain

Your AI-powered knowledge management system.

## What Is This?

This is a Second Brain — a personal knowledge management system built on Obsidian and powered by AI agents. It uses the PARA method (Projects, Areas, Resources, Archive) to organize everything in your life into one connected, searchable, intelligent system.

Think of it as an extension of your memory. Every note, idea, project, and piece of knowledge lives here, connected to everything else through wiki-links and Maps of Content (MOCs).

## Quick Start

### 1. Open the Vault

Open this folder in Obsidian. The vault root is this directory.

### 2. Start with the Dashboard

Open [[Dashboard]] — it shows your active projects, intelligence reports, and quick links to everything.

### 3. Capture Your First Note

Press `Ctrl+N` (or `Cmd+N` on Mac) to create a new note. The template system will help you format it.

### 4. Explore the Structure

| Folder | Purpose |
|--------|---------|
| [[00-Inbox/Index\|00-Inbox]] | Capture point — dump everything here first |
| [[01-projects/Index\|01-Projects]] | Active projects with goals and deadlines |
| [[02-areas/Index\|02-Areas]] | Life areas you maintain ongoing |
| [[03-resources/Index\|03-Resources]] | Reference material and knowledge base |
| [[04-archive/Index\|04-Archive]] | Completed or deprecated content |
| [[05-people/Index\|05-People]] | Contacts and relationships |
| [[06-meetings/Index\|06-Meetings]] | Meeting notes by date |
| [[07-daily/Index\|07-Daily]] | Daily notes and reflections |

### 5. Use AI Agents

Type a trigger command to activate an agent:

| Command | Agent | What It Does |
|---------|-------|--------------|
| `/plan` or `setup` | Architect | Scaffold vault structure, create MOCs |
| `/capture` or `save` | Scribe | Capture raw text into inbox |
| `/search` or `find` | Seeker | Vault-wide information retrieval |
| `/connect` or `link` | Connector | Build relationships between notes |
| `/audit` or `check` | Librarian | Cleanup, dedup, health checks |
| `/sync` or `mail` | Postman | Gmail and Calendar integration |
| `/strategy` or `goals` | Strategist | Align tasks with long-term goals |
| `/draft` or `write` | Ghostwriter | Voice-mimic drafting |
| `/critic` or `security` | Auditor | Adversarial review and security |
| `/research` or `web` | Researcher | Automated web research |
| `/pulse` or `digest` | Pulse | Daily summary generation |
| `/bridge` or `code` | Bridge | Sync notes with codebase |

## Example Workflows

### Workflow 1: Capture and Process a Meeting

```
1. After a meeting, type: /capture
2. Agent (Scribe) creates a note in 00-Inbox/Meeting-2026-06-04.md
3. Note uses the Meeting template with attendees, agenda, decisions, action items
4. Later, type: /inbox-triage
5. Agent (Sorter) moves the note to 06-meetings/2026/06-04-meeting.md
6. Agent (Connector) links attendees to 05-people/ and action items to 01-projects/
```

### Workflow 2: Start a New Project

```
1. Type: /plan
2. Agent (Architect) asks about the project
3. You describe: name, goal, deadline, team
4. Agent creates:
   - 01-projects/your-project/Overview.md
   - 01-projects/your-project/Tasks.md
   - 01-projects/your-project/Context.md
   - 01-projects/your-project/Activity-Log.md
5. Updates 01-projects/Index.md with the new project
6. Updates MOC-root-projects.md
```

### Workflow 3: Research a Topic

```
1. Type: /research AI agents in healthcare
2. Agent (Researcher) searches the web
3. Finds papers, articles, GitHub repos
4. Creates structured notes in 03-resources/AI-Knowledge/
5. Links to related notes via Connector
6. Updates MOC-root-resources.md
```

### Workflow 4: Daily Review

```
1. Type: /pulse
2. Agent (Pulse) generates a daily digest:
   - What you worked on today
   - Upcoming deadlines
   - Inbox items to process
   - Notes created or modified
3. You review and plan tomorrow
```

### Workflow 5: Weekly Maintenance

```
1. Type: /audit
2. Agent (Librarian) runs health checks:
   - Broken links found and fixed
   - Duplicate notes merged
   - Orphan notes linked
   - Tag taxonomy updated
   - Stale content archived
3. You get a health report
```

### Workflow 6: Code-to-Notes Sync

```
1. Working on a project, type: /bridge
2. Agent (Bridge) reads your codebase
3. Extracts: API endpoints, database schemas, architecture decisions
4. Creates notes in 03-resources/Codebase/
5. Links code references to project notes
```

## Templates

The vault includes 15 templates for different note types:

| Template | Use For |
|----------|---------|
| Daily Note | Daily journal, tasks, reflections |
| Journal Entry | Detailed journal entries |
| Meeting | Meeting notes with agenda and action items |
| Project | Project overview and tracking |
| Task | Individual task tracking |
| Goal | Goal setting with milestones |
| Idea | Quick idea capture |
| Book | Book notes and summaries |
| Course | Course notes and progress |
| Thesis Note | Academic research notes |
| Budget Entry | Financial tracking |
| Investment | Investment portfolio |
| Work Log | Daily work logging |
| Weekly Review | Weekly reflection and planning |
| Note | General-purpose note |

## Navigation

### Maps of Content (MOCs)

MOCs are index pages that connect related notes. Start here:

- [[MOC-root]] — Master index
- [[MOC-root-projects]] — All projects
- [[MOC-root-resources]] — All resources
- [[MOC-root-skills|Skills Map]] — All AI skills

### Wiki-Links

Connect notes using double brackets: `[[Note Title]]`

Example: "This relates to [[Dashboard]] and [[01-projects/Index|Projects]]"

### Graph View

Open Obsidian's Graph View (`Ctrl+G`) to see how everything connects. The more links you create, the more useful the graph becomes.

## AI Integration

This vault works with multiple AI tools:

| Tool | Config File | Purpose |
|------|-------------|---------|
| Claude Code | `CLAUDE.md` | Primary AI router |
| Cursor | `.cursorrules` | IDE integration |
| Windsurf | `.windsurfrules` | IDE integration |
| GitHub Copilot | `.github/copilot-instructions.md` | VS Code AI |
| Codex | `.codex/` | OpenAI integration |

All tools read from the same vault and follow the same governance rules defined in [[MASTER_AI_RULES]].

## Security and Governance

- [[MASTER_AI_RULES]] — The single source of truth for all AI operations
- Credentials stored in environment variables (never in files)
- Automated backup daily at 22:00
- Health checks via `vault-health-check.py`

## Getting Help

- Ask an agent: "help me with [topic]"
- Run `/audit` to check vault health
- Check [[ARCHITECTURE]] for system design details
- See [[CHANGELOG]] for recent changes

---

*Built with Obsidian, powered by AI agents.*
