---
status: active
project: skill-loader
---

# Skill Auto-Loader (Second Brain)

Hydrate only the skills that match the current task. Never load all skills into context.

## Skill Source

- Root: `~/.claude/skills` → symlink → `Documents/ObsidianVault/Second Brain/brain/skills-universal/`
- Total local skills: 26 SKILL.md files (verified 2026-06-02). External registry entries point to GitHub repos and are NOT local.
- Lockfile: `~/.agents/.skill-lock.json` tracks external installs.

## Loading Rules

1. **Read the user request once.** Identify intent in 1-2 keywords.
2. **Match against skill descriptions only.** Skill frontmatter `description:` is the index. Do NOT read full SKILL.md until matched.
3. **Load maximum 3 skills per turn.** If 4+ match, pick the top 3 by relevance.
4. **Skill is loaded = `Read` tool called on `SKILL.md`.** Reading is the trigger. Caching is automatic.
5. **No skill → answer directly.** Do not invent skill names. Do not load skills for generic tasks.

## Trigger Phrases → Skill Map

| User says | Skill |
|-----------|-------|
| caveman, terse, brief, less tokens, /caveman | `caveman` |
| compress memory, /caveman:compress, compact | `compress` |
| commit, git commit | `caveman-commit` |
| review code, PR review | `caveman-review` |
| stats, token report | `caveman-stats` or `pordee-stats` |
| tdd, test first, red green | `rtk-tdd` |
| triage issues, sprint triage | `rtk-triage` |
| lean-ctx, context budget | `lean-ctx` |
| idea, refine thought | `idea-refine` |
| plan, breakdown, tasks | `planning-and-task-breakdown` |
| research, web search | `web-search` or `deep-research` |
| security audit, vulnerability | `security-review` or `security-scan` |
| design pattern | `design-patterns` |
| simplify code | `code-simplification` or `code-simplifier` |
| pdf, docx, pptx, xlsx | matching file skill |
| api design | `api-design` |
| ADR, architecture decision | `architecture-decision-records` |
| monorepo navigate | `monorepo-navigator` |
| doubt, edge case | `doubt-driven-development` |
| thai token, tto | `thai-token-optimizer` |
| pordee lite, pordee full | `pordee` |
| mcp build | `mcp-builder` |
| plugin create | `plugin-creator` |
| skill create | `skill-creator` |
| rule distill | `rules-distill` |
| strategic compact | `strategic-compact` |
| tech debt | `tech-debt-tracker` |
| tech stack eval | `tech-stack-evaluator` |
| token budget | `token-budget-advisor` or `context-budget` |
| adversarial review | `adversarial-reviewer` |
| agent workflow | `agent-workflow-designer` |
| ai engineering | `ai-first-engineering` |
| ai security | `ai-security` |
| autonomous agent | `autonomous-agent-harness` |
| code reviewer | `code-reviewer` |
| design system | `design-system` |
| context engine | `context-engine` |

## Hard Rules

- Never load more than 3 skills per response.
- Never load a skill whose description doesn't match the task.
- Never claim a skill exists unless you have read its `SKILL.md` path in this session.
- Reading a skill twice costs ~13 tokens — track and avoid.

## Token Budget

- 0 tokens: detect intent (use existing context)
- ~50 tokens: frontmatter-only index lookup
- ~500-1500 tokens: full SKILL.md for matched skills (1-3)
- 0 tokens: cached re-use within session
