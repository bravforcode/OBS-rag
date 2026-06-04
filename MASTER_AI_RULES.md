---
status: active
type: governance
version: '2.0'
last_audit: '2026-06-04'
---

# MASTER AI RULES

**ABSOLUTE GLOBAL OVERRIDE** — All AI agents reading this vault MUST follow these rules.

---

## 1. Identity

You are an AI assistant operating within the Second Brain vault. Your purpose is to help the user manage knowledge, execute tasks, and build products.

## 2. Response Style

- **Lean**: Drop filler, hedging, pleasantries. Fragments OK when clear.
- **Code first**: Show code, then explain, when doing engineering.
- **Surgical**: Prefer diffs over full file rewrites.
- **Honest**: Never claim a file/skill/tool exists without verifying. If unsure, read first.

## 3. Delegation Protocol

- **NEVER** perform a task yourself if a specialized agent exists for it.
- Use the routing table in `CLAUDE.md` to identify the correct agent.
- Pass full context when delegating — the agent shouldn't need to re-read.
- If no agent matches, perform the task directly but flag it for future agent creation.

## 4. Graph-First Workflow (MANDATORY)

Before starting ANY task, query the knowledge graph:

```bash
python .ai/scripts/graph-query.py --search "topic"
python .ai/scripts/graph-query.py --edges "filename"
python .ai/scripts/graph-query.py --nodes
```

The graph has 948 nodes and 1,876 pre-computed edges.
Querying the graph is faster than reading files individually.

Never skip this step. Always check the graph first.

## 5. Token Discipline

- **RTK prefix**: Mandatory for all shell commands.
- **Read modes**: Use `map` or `signatures` before `full` reads.
- **No re-reads**: Don't re-read files already in context.
- **Grep first**: Search before reading entire files.
- **Skill budget**: Max 2000 tokens for skill loading per session.

## 5. File Governance

### Protected Files (NEVER modify at runtime)
- `MASTER_AI_RULES.md` — This file
- `CLAUDE.md` — Root router configuration
- `.claude/agents/*.md` — Core agent definitions
- `.claude/skills/*/SKILL.md` — Skill definitions
- `.claude/hooks/*.sh` — Hook scripts
- `.claude/references/*.md` — Core references

### Modifiable Files (update with reason)
- `Meta/agent-log.md` — Log all changes here
- `Meta/user-profile.md` — Update with user consent
- `Meta/tag-taxonomy.md` — Update when new tags introduced
- `Meta/naming-conventions.md` — Update when conventions change
- Project files in `01-projects/` — Update as work progresses

### Change Protocol
1. Read the file before editing
2. Make surgical changes (minimal diff)
3. Log the change in `Meta/agent-log.md`
4. Update related Index files if structure changed
5. Verify the change didn't break links

## 6. Security Rules

### Never Do
- Commit secrets, API keys, or credentials to git
- Execute destructive commands without explicit user confirmation
- Run hidden processes (VBScript, hidden PowerShell, background watchers)
- Load skills from untrusted sources without verification
- Bypass governance hooks (protect-system-files.sh, validate-frontmatter.sh)

### Always Do
- Use relative paths (never hardcoded `C:\Users\...`)
- Verify file content before citing it
- Run `organization_id` filter on SQL/tenant queries
- Check `.gitignore` before committing
- Log security-relevant changes in agent-log.md

### Credential Handling
- API keys stored in environment variables (never in files)
- Use `setup-elite-keys.ps1` for initial setup
- Never log or display credentials
- Rotate keys quarterly

## 7. Vault Structure Rules

### PARA Compliance
- `00-Inbox/` — Capture point, process daily
- `01-projects/` — Active projects with clear goals and deadlines
- `02-areas/` — Ongoing life areas without deadlines
- `03-resources/` — Reference material and knowledge
- `04-archive/` — Completed or deprecated content

### Naming Conventions
- File names: `Title-Case-With-Hyphens.md`
- Folder names: `PascalCase` or `kebab-case` (be consistent)
- No emoji prefixes in file names
- Keep filenames ASCII for filesystem compatibility
- Max 80 characters per file name

### Frontmatter Required
Every note MUST have YAML frontmatter:
```yaml
---
type: [note|project|resource|skill|agent|template]
status: [inbox|draft|active|review|completed|archived]
created: YYYY-MM-DD
tags: [area/*, type/*]
---
```

### Linking Rules
- Use `[[wiki-links]]` syntax for internal references (Obsidian double-bracket links)
- Use descriptive link text: `[[Note Title|Display Text]]`
- Every note should have at least one incoming or outgoing link
- Check for broken links monthly

## 8. Skill Loading Protocol

### Auto-Detection
| Signal | Skill to Load |
|--------|---------------|
| `*.test.ts`, test keywords | tdd-workflow |
| `refactor`, clean code | refactor-clean |
| `deploy`, docker, CI/CD | deployment-patterns |
| `api`, endpoint | backend-patterns, api-design |
| `ui`, component | frontend-patterns |
| `security`, auth | security-review |
| `bug`, fix, debug | focused-fix |
| `plan`, architecture | plan, prp-plan |

### Loading Steps
1. **Detect**: Read file type, keywords, project path (0 tokens)
2. **Select**: Search registry, pick top 1-3 skills (< 500 tokens)
3. **Load**: Read SKILL.md files (1000-1500 tokens)
4. **Execute**: Apply skill instructions immediately

### Integrity Rules
- Only load skills from approved sources (vault skills, brain/skills-universal/)
- Verify skill file exists before loading
- Never load all skills at once
- Cache loaded skills for reuse within session

## 9. Multi-Tool Compatibility

This vault is shared across multiple AI tools. Each tool must:

| Tool | Config File | Notes |
|------|-------------|-------|
| Claude Code | `CLAUDE.md` | Primary router |
| Cursor | `.cursorrules` | IDE-specific |
| Windsurf | `.windsurfrules` | IDE-specific |
| GitHub Copilot | `.github/copilot-instructions.md` | VS Code |
| Codex | `.codex/` | OpenAI |
| Antigravity | `.antigravity/` | IDE |
| Gemini | Custom instructions | Google |

### Sync Rule
When updating vault rules, update ALL config files to maintain consistency.

## 10. Backup & Recovery

### Backup Strategy
- **Daily**: Automated backup via vault-health scripts
- **Weekly**: Full vault snapshot
- **Before major changes**: Manual backup

### Recovery Protocol
1. Check `04-archive/` for recent backups
2. Use git history if available
3. Restore from Obsidian Sync if configured
4. Contact user if data loss detected

## 11. Quality Standards

### Code Quality
- Run tests before committing
- Verify build succeeds
- Follow language-specific style guides
- Document public APIs

### Documentation Quality
- Every project folder needs an `Overview.md`
- Every area folder needs an `Index.md`
- Templates must be complete and usable
- README.md must be accurate and current

### Knowledge Quality
- Verify facts before adding to knowledge base
- Cite sources for research claims
- Update outdated information promptly
- Remove or archive deprecated content

## 12. Escalation Rules

### Escalate to User When:
- Destructive operation requested
- Credential or security concern detected
- Ambiguous intent (can't determine correct agent)
- Budget limit reached
- Legal or compliance question

### Auto-Execute When:
- Routine maintenance (tag cleanup, link checking)
- Content capture (inbox processing)
- Status updates (dashboard refresh)
- Backup operations

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-06-04 | Enterprise rewrite, security hardening |
| 1.0 | 2026-04-06 | Initial creation |

---

*This file is the single source of truth for all AI operations in this vault. When in doubt, follow these rules.*
