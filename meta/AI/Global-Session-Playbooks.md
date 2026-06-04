---
status: unprocessed
project: unknown
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:55.777206'
---

---
type: playbook-catalog
scope: global
updated: 2026-04-09
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
---# Global Session Playbooks

## Bug Fix
match: bug, fix, error, failing, regression, broken, debug
skills:
- playwright
- tdd-workflow
rules:
- Reproduce before changing code.
- Prefer a root-cause fix over a symptom patch.
checklist:
- Confirm current behavior and expected behavior
- Inspect related routes/services/components
- Add or update verification
note-hints:
- active-tasks
- agent-log
- architecture
category-boosts:
- task: 14
- architecture: 10
- agent-log: 8

## Deployment
match: deploy, production, preview, release, env, vercel, infra
skills:
- vercel-deploy
- render-deploy
rules:
- Check infra manifest and environment keys before deploying.
checklist:
- Verify required env vars
- Run build locally
- Check logs or preview URL after deploy
note-hints:
- infra
- health
- architecture
category-boosts:
- resource: 12
- health: 10
- architecture: 6

## Security Review
match: security, auth, token, secret, permission, role, jwt
skills:
- security-best-practices
rules:
- Read security notes and auth-related architecture before editing.
checklist:
- Check access control paths
- Check secret handling and sanitizer impact
- Verify privilege boundaries
note-hints:
- security
- auth
- backend
category-boosts:
- security: 18
- architecture: 10
- rule: 6

## 🔗 Semantic Connections
- [[Session-Playbooks]]
- [[Playbook-Suggestions]]
- [[Playbook-Suggestions]]
