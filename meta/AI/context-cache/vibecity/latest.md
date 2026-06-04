---
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
status: unprocessed
project: unknown
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:55.880151'
---

# VibeCity
Root: C:\vibecity.live
Folder: VibeCity | Search: fts-only | Policy: full-auto

## Notes
- **Automation Commands**: Automation Commands | This note complements `commands.json` in the cache. | Auto Commands
- **Skill Sources**: Skill Sources | This note lists lazy-load skills for VibeCity. | Auto Skill Sources
- **Session Startup**: Session Startup | 1. Read `preflight.md` | Auto Startup Protocol
- **Playbook Suggestions**: Playbook Suggestions | Keep manual commentary above the auto block below. | Observed Signals | Suggested Playbooks | Bug Fix Flow | Signal: `bug-fix` | Confide…

## Knowledge
- **Model Context Protocol**: Model Context Protocol | Summary | Related Topics | [[Agent Engineering|Agent Engineering]] | [[03-resources/AI-Knowledge/Topi…

## Skills
- **api-design**: API Design Skill | Design Principles | **RESTful semantics**: Correct HTTP verbs, status codes, resource naming | **Contract-first**: OpenAPI spec drives imple… (C:\vibecity.live\skills\api-design\SKILL.md)
- **database-ops**: Database Ops Skill | Core Principles | **Schema stability**: Get it right early — migrations are painful to undo | **Index everything you filter/sort by** — bu… (C:\vibecity.live\skills\database-ops\SKILL.md)
- **devops-pipeline**: DevOps Pipeline Skill | Core Philosophy | **Speed first**: Maximize cache hits, parallelize jobs, minimize cold starts | **Security baked in**: Non-root contai… (C:\vibecity.live\skills\devops-pipeline\SKILL.md)
- **fullstack-scaffold**: Full Stack Scaffold Skill | Core Deliverables | Stack Detection | **Frontend**: Next.js / React / Vue / Svelte / Astro | **Backend**: Node/Express/NestJS / Fas… (C:\vibecity.live\skills\fullstack-scaffold\SKILL.md)
- **git-workflow**: Git Workflow Skill | Branching Strategy Selection | GitHub Flow (Recommended for most teams) | `main` is always deployable | Every change comes through a PR |… (C:\vibecity.live\skills\git-workflow\SKILL.md)
- **infra-as-code**: Infrastructure as Code Skill | Core Principles | **State is sacred** — remote state in S3+DynamoDB (AWS) or GCS (GCP) | **Modules for reuse** — don't repeat re… (C:\vibecity.live\skills\infra-as-code\SKILL.md)

## Commands
- `npm run dev` [dev/low]
- `npm run build` [build/low]
- `npm run build:e2e` [build/low]
- `npm run preview` [dev/low]
- `npm run preview:e2e` [custom/medium]
- `npm run data:sync:nationwide` [custom/medium]
- `npm run check` [lint/low]
- `npm run check:bundle` [custom/medium]
- `npm run format` [lint/low]
- `npm run lint` [lint/low]

## 🔗 Semantic Connections
- [[preflight]]
- [[Skill-Sources]]
- [[latest]]
