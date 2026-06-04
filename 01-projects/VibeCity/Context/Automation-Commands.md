---
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
status: unprocessed
project: VibeCity
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.407171'
---

# Automation Commands

This note complements `commands.json` in the cache.

<!-- AUTO-SYNC:START -->
## Auto Commands

Related: [[_VibeCity Dashboard|VibeCity Dashboard]] · [[AI Knowledge Hub|AI Knowledge Hub]]

| Label | Kind | Risk | Command |
|-------|------|------|---------|
| dev | dev | low | `npm run dev` |
| build | build | low | `npm run build` |
| build:e2e | build | low | `npm run build:e2e` |
| preview | dev | low | `npm run preview` |
| preview:e2e | custom | medium | `npm run preview:e2e` |
| data:sync:nationwide | custom | medium | `npm run data:sync:nationwide` |
| check | lint | low | `npm run check` |
| check:bundle | custom | medium | `npm run check:bundle` |
| format | lint | low | `npm run format` |
| lint | lint | low | `npm run lint` |
| lint:fix | custom | medium | `npm run lint:fix` |
| build:roads:cm | build | low | `npm run build:roads:cm` |
| build:roads:cm:lanes | build | low | `npm run build:roads:cm:lanes` |
| snapshot:localhost | custom | medium | `npm run snapshot:localhost` |
| storybook | dev | low | `npm run storybook` |
| build-storybook | build | low | `npm run build-storybook` |
| test:unit:coverage | test | low | `npm run test:unit:coverage` |
| test:unit | test | low | `npm run test:unit` |
| playwright:install | custom | medium | `npm run playwright:install` |
| test:e2e | test | low | `npm run test:e2e` |
| test:e2e:ui | test | low | `npm run test:e2e:ui` |
| test:e2e:smoke | test | low | `npm run test:e2e:smoke` |
| test:e2e:mobile-contracts | test | low | `npm run test:e2e:mobile-contracts` |
| test:e2e:smoke-map-lite | test | low | `npm run test:e2e:smoke-map-lite` |

Source of truth: `Meta/AI/context-cache/vibecity/commands.json`
<!-- AUTO-SYNC:END -->

## 🔗 Semantic Connections
- [[Automation-Commands]]
- [[latest]]
- [[preflight]]
