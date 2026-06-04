---
status: unprocessed
project: unknown
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:55.728573'
---

### Learning
**Purpose**: Capture courses, books, certifications, and self-directed learning.

**Sub-folders**:
- `Courses/` — Online courses, materials, progress, certificates
- `Books/` — Book notes, summaries, key takeaways, reading list
- `Certifications/` — Cert progress, exams, requirements

**Templates**: Course, Book, Task, Note

---

### Research
**Purpose**: Manage academic research, thesis writing, literature review, and research notes (English + Thai).

**Sub-folders**:
- `Thesis/` — Thesis drafts, structure, chapter notes, progress
- `Literature Review/` — Papers, sources, annotations, reference library
- `Notes/` — Research ideas, findings, hypotheses (supports both languages)

**Templates**: Thesis Note, Literature Note, Research Idea, Meeting (for advisor meetings)

---

### Personal
**Purpose**: Personal goals, journaling, daily reflections, gratitude practice.

**Sub-folders**:
- `Goals/` — Personal goals, milestones, progress tracking
- `Journal/` — Daily journal entries, reflections, gratitude logs

**Templates**: Journal Entry, Goal, Weekly Review, Daily Note

---

### Finance
**Purpose**: Track budget, expenses, income, and investments comprehensively.

**Sub-folders**:
- `Budget/` — Monthly budgets, financial planning, projections
- `Expenses/` — Expense logs, spending tracking, receipt notes
- `Income/` — Freelance income, invoices, multi-source tracking
- `Investments/` — Portfolio tracking, savings goals, investment analysis

**Templates**: Budget Entry, Investment, Expense Log

---

## Core Folders

### 00-Inbox
**Purpose**: Daily capture point for all incoming information (Scribe creates notes here).

**Agent**: Scribe creates new notes here. Sorter triages and moves to correct areas.

**Retention**: Empty regularly via `/inbox-triage` skill or Sorter agent.

---

### 01-Projects
**Purpose**: Project index across all areas.

**Notes**: Can contain active projects from any area (Work, Learning, Research, Personal). Links to specific area projects.

---

### 03-Resources
**Purpose**: Reference materials, templates, external resources, tools.

**Examples**: Tool guides, style guides, frameworks, links, checklists.

---

### 04-Archive
**Purpose**: Completed projects, old notes, obsolete information.

**Agent**: Architect or Sorter moves completed items here when no longer active.

---

### 05-People
**Purpose**: Contact information, relationship notes, networking log.

**Template**: Person.md — name, role, contact, last interaction, notes.

---

### 06-Meetings
**Purpose**: Meeting notes, organized by year.

**Current**: 2026/ (auto-created each January)

**Template**: Meeting.md — attendees, agenda, decisions, action items, follow-up.

---

### 07-Daily
**Purpose**: Daily notes, reflections, day-specific planning.

**Template**: Daily Note.md — intention, tasks, end-of-day reflection.

---

### MOC (Maps of Content)
**Purpose**: Navigation and overview for each area and the vault as a whole.

**Files**:
- `Index.md` — Master MOC, entry point, links to all area MOCs
- `Work.md`, `Learning.md`, `Research.md`, `Personal.md`, `Finance.md` — Area MOCs

**Pattern**: Each MOC lists key notes, active projects, structure, and related MOCs.

---

## Meta Folder — Vault Governance

**user-profile.md** — Single source of truth (read by all agents)
- User preferences, language, active agents, integrations

**vault-structure.md** — This file
- Canonical folder structure and documentation

**naming-conventions.md** — File naming rules
- How to name notes, folders, areas (enforced by linters/agents)

**tag-taxonomy.md** — Official tag list
- All valid tags, hierarchy, area-specific tags (prevents tag sprawl)

**agent-log.md** — Change log
- Record of all automated changes made by agents (Architect, Sorter, Librarian, etc.)

**health-reports/** — Weekly audits
- Librarian creates health reports (duplicates, orphans, stale content)

**states/** — Agent post-its
- Each agent has a `.md` file to persist state, last-run, resumable flows

---

## Updates to This File

This is a living document. When new areas, folders, templates, or agents are added:

1. Update this file to reflect the change
2. Update `tag-taxonomy.md` if new tags are introduced
3. Update `agent-log.md` to record the change
4. If a new MOC is created, update `MOC/Index.md` to link to it

**Last Updated**: 2026-04-06 (Architect, onboarding)

## 🔗 Semantic Connections
- [[tag-taxonomy]]
- [[agent-log]]
- [[naming-conventions]]
