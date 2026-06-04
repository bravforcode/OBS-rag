---
status: unprocessed
project: TaskAm
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.278328'
---

# Automation Commands

This note complements `commands.json` in the cache.

<!-- AUTO-SYNC:START -->
## Auto Commands

Related: [[_TaskAm Dashboard|TaskAm Dashboard]] · [[AI Knowledge Hub|AI Knowledge Hub]]

| Label | Kind | Risk | Command |
|-------|------|------|---------|
| dev | dev | low | `npm run dev` |
| dev:fe | custom | medium | `npm run dev:fe` |
| dev:be | custom | medium | `npm run dev:be` |
| build | build | low | `npm run build` |
| build:be | build | low | `npm run build:be` |
| lint | lint | low | `npm run lint` |
| test:root | test | low | `npm run test:root` |
| test | test | low | `npm run test` |
| clean | custom | medium | `npm run clean` |
| deploy:production | custom | high | `npm run deploy:production` |
| test:e2e | test | low | `npm run test:e2e` |
| test:e2e:real | test | low | `npm run test:e2e:real` |
| test:cross-browser | test | low | `npm run test:cross-browser` |
| test:functional | test | low | `npm run test:functional` |
| test:performance:smoke | test | low | `npm run test:performance:smoke` |
| test:performance:load | test | low | `npm run test:performance:load` |
| test:performance:stress | test | low | `npm run test:performance:stress` |
| test:performance:spike | test | low | `npm run test:performance:spike` |
| test:performance:endurance | test | low | `npm run test:performance:endurance` |
| test:performance:all | test | low | `npm run test:performance:all` |
| verify:deployment | custom | high | `npm run verify:deployment` |
| orchestrate:deployment | custom | high | `npm run orchestrate:deployment` |
| audit:security | custom | medium | `npm run audit:security` |
| health:check | custom | medium | `npm run health:check` |

Source of truth: `Meta/AI/context-cache/taskam/commands.json`
<!-- AUTO-SYNC:END -->
