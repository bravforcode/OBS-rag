---
status: active
type: taxonomy
last_audit: '2026-06-04'
---

# Tag Taxonomy

Official tag hierarchy for the Second Brain vault. All notes MUST use tags from this taxonomy.

## Area Tags (Life Domains)

| Tag | Usage |
|-----|-------|
| `#area/work` | Professional projects, freelance, job-related |
| `#area/learning` | Courses, books, certifications, self-study |
| `#area/research` | Academic research, thesis, literature review |
| `#area/personal` | Personal goals, journal, health, habits |
| `#area/finance` | Budget, expenses, income, investments |
| `#area/dev-practice` | Coding skills, tools, workflows |

## Type Tags (Content Type)

| Tag | Usage |
|-----|-------|
| `#type/project` | Active project notes |
| `#type/note` | General notes, ideas |
| `#type/resource` | Reference material, how-to guides |
| `#type/journal` | Daily/weekly journal entries |
| `#type/meeting` | Meeting notes and minutes |
| `#type/task` | Action items, todos |
| `#type/decision` | ADRs, architectural decisions |
| `#type/lesson` | Lessons learned, retrospective |
| `#type/dashboard` | Overview/status pages |
| `#type/template` | Reusable templates |
| `#type/skill` | AI skill definitions |
| `#type/agent` | Agent manual/definition |
| `#type/intelligence` | Analysis reports, research synthesis |

## Status Tags

| Tag | Usage |
|-----|-------|
| `#status/inbox` | Recently created, not yet filed |
| `#status/draft` | Work in progress |
| `#status/active` | Current, in use |
| `#status/review` | Needs review or approval |
| `#status/completed` | Done, finished |
| `#status/archived` | No longer relevant |
| `#status/deprecated` | Superseded by newer version |

## Priority Tags

| Tag | Usage |
|-----|-------|
| `#priority/critical` | Urgent, must do now |
| `#priority/high` | Important, do soon |
| `#priority/medium` | Normal priority |
| `#priority/low` | Nice to have |

## Topic Tags (Knowledge Domains)

| Tag | Usage |
|-----|-------|
| `#topic/ai-ml` | AI, machine learning, LLMs |
| `#topic/web-dev` | Frontend, backend, fullstack |
| `#topic/devops` | CI/CD, Docker, deployment |
| `#topic/security` | Security, auth, encryption |
| `#topic/database` | SQL, NoSQL, data modeling |
| `#topic/mobile` | iOS, Android, React Native |
| `#topic/api` | REST, GraphQL, gRPC |
| `#topic/testing` | TDD, QA, automation |

## Language Tags

| Tag | Usage |
|-----|-------|
| `#language/en` | English content |
| `#language/th` | Thai content |

## Project Tags

| Tag | Usage |
|-----|-------|
| `#project/taskam` | TaskAm project |
| `#project/vibecity` | VibeCity project |
| `#project/graxia` | Graxia OS project |
| `#project/bravos` | BravOS project |
| `#project/testlyn` | Testlyn project |
| `#project/plexta` | Plexta project |

## Tool Tags

| Tag | Usage |
|-----|-------|
| `#tool/obsidian` | Obsidian-specific |
| `#tool/claude` | Claude Code specific |
| `#tool/cursor` | Cursor IDE specific |
| `#tool/copilot` | GitHub Copilot specific |
| `#tool/mcp` | MCP server related |

## Tag Rules

1. **Minimum 2 tags**: Every note must have at least one area tag and one type tag
2. **Maximum 8 tags**: Prevent tag bloat
3. **No synonyms**: Use only one form (e.g., `#type/note` not `#type/notes`)
4. **Lowercase only**: All tags are lowercase with hyphens
5. **Hierarchical**: Use `/` separator for hierarchy

## Tag Maintenance

The Librarian agent runs weekly audits to detect:
- Unused tags (used fewer than 2 times)
- Near-duplicate tags (e.g., `#book` and `#books`)
- Orphan tags (tags not in this taxonomy)

**Last Audit**: 2026-06-04 (Auditor, deep dive)

---

## Updates to This Taxonomy

If tags change:
1. Update this file
2. Update `Meta/agent-log.md` to record the change
3. Librarian can batch-retag notes if needed
4. New notes follow updated taxonomy automatically

## Semantic Connections
- [[naming-conventions]]
- [[vault-structure]]
- [[agent-log]]
