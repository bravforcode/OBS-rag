---
version: 2.0.0
status: active
token_budget: adaptive (300-2000)
last_updated: 2026-04-28
---

# Smart Skill System (Unified)

ระบบโหลดสกิลอัจฉริยะที่ทำงานกับ Claude Code, Codex, Gemini, Cursor, Windsurf, Antigravity

---

## 🎯 หลักการทำงาน

1. **Auto-Detect**: วิเคราะห์ context จากสิ่งที่ user กำลังทำ
2. **Smart Select**: เลือกสกิลที่เหมาะสมที่สุด (1-3 สกิล)
3. **Token-Efficient**: โหลดแค่ที่จำเป็น ประหยัดโทเคน
4. **Cross-Tool**: ใช้งานได้กับทุก AI tool ด้วยระบบเดียวกัน

---

## 🚀 วิธีใช้

### Trigger Words (พูดอะไรก็ได้)
- "ใช้สกิล" / "use skills"
- "ช่วยด้วย" + คำบรรยายงาน
- หรือแค่เริ่มทำงาน → AI จะ auto-detect เอง

### ตัวอย่าง
```
User: "ช่วยเทส API ให้หน่อย"
AI: [Auto-load tdd-workflow + backend-patterns] → เริ่มทำทันที

User: "refactor โค้ดนี้ให้หน่อย"
AI: [Auto-load refactor-clean + code-review] → เริ่ม refactor

User: "deploy ขึ้น production"
AI: [Auto-load deployment-patterns + security-checklist] → เริ่ม deploy
```

---

## 🧠 Detection Matrix

| สัญญาณจาก Context | สกิลที่โหลด | Confidence |
|-------------------|-------------|------------|
| `.test.ts`, `.spec.py` | tdd-workflow | 95% |
| `refactor`, `clean up` | refactor-clean | 90% |
| `deploy`, `docker`, `CI/CD` | deployment-patterns | 90% |
| `api`, `endpoint` | backend-patterns, api-design | 85% |
| `ui`, `component`, `css` | frontend-patterns, ui-ux-pro-max | 85% |
| `security`, `auth` | security-review | 90% |
| `bug`, `fix`, `debug` | focused-fix, gsd:debug | 90% |
| `plan`, `design` | plan, prp-plan | 85% |
| `pdf`, `docx` | pdf, docx | 95% |
| `performance`, `slow` | performance-checklist | 85% |

---

## 🛠️ Integration ตาม Tool

### Claude Code (VS Code Extension)
**ไฟล์:** `CLAUDE.md` (อยู่ใน root ของ project)
```markdown
## Smart Skill System

เมื่อ user พูดถึง skill หรือ task match skill pattern:
1. Read `C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal\skills-router.md`
2. Search `skills-registry-compact.json` for relevant skills
3. Load 1-3 matching SKILL.md files
4. Execute using loaded skill instructions

Auto-detect from:
- File extensions: .tsx → frontend, .py → backend, .test.* → testing
- Keywords in request
- Project path (graxia-os, vibecity, taskam)
```

### Cursor
**ไฟล์:** `.cursorrules` (root ของ project)
```
When user says "use skills" or task matches known patterns:
1. Check local vault: C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal
2. Load relevant SKILL.md based on file type and keywords
3. Follow skill instructions for the task
```

### Windsurf
**ไฟล์:** `.windsurfrules` (root ของ project)
```
- Smart skill loading enabled
- Auto-detect from context
- Load from: C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal
```

### Claude.ai (Web)
**Custom Instructions:**
```
I have a local skill hub at:
C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal

When I ask to "use skills" or when a task clearly matches a skill:
1. Ask me to paste the relevant SKILL.md file
2. Or tell me which skill to use from the 1390 available

Skills are organized by category: testing, deployment, security, frontend, backend, etc.
```

### Gemini (Claude.ai interface)
**Custom Instructions:** เหมือน Claude.ai

### Antigravity
**ไฟล์:** `.antigravity/config.yaml`
```yaml
skill_system:
  enabled: true
  source: "C:\\Users\\menum\\Documents\\ObsidianVault\\Second Brain\\brain\\skills-universal"
  auto_detect: true
  max_skills_per_session: 3
```

### GitHub Copilot / Codex
**ไฟล์:** `.github/copilot-instructions.md`
```markdown
## Skill Integration

This project uses skills from:
`C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal`

When suggesting code or helping with tasks, reference these skills:
- For testing: tdd-workflow, testing-patterns
- For API: backend-patterns, api-design
- For UI: frontend-patterns, design-system
- For deployment: deployment-patterns, ci-cd
```

---

## 📊 Token Efficiency

### ก่อนใช้ Smart Loader
- โหลดสกิลทุกครั้ง: ~3000-5000 tokens
- ไม่แน่ใจว่าจะใช้สกิลไหน: ~1000 tokens (สับสน)

### หลังใช้ Smart Loader
- Auto-detect: ~0 tokens (ใช้ context ที่มี)
- Load 1 skill: ~1000 tokens
- Load 2 skills: ~1500 tokens
- Cache สกิลที่ใช้แล้ว: ~0 tokens (session)

**ประหยัดโทเคน: 50-70%**

---

## 🔧 Files & Paths

| File | Path |
|------|------|
| Smart Loader | `brain/skills-universal/_smart-skill-loader/SKILL.md` |
| Skill Router | `brain/skills-universal/skills-router.md` |
| Registry | `brain/skills-universal/skills-registry-compact.json` |
| AI Gateway Config | `brain/ai-gateway/config.json` |
| Agent Adapters | `Meta/AI/Agent-Adapters.md` |
| Project Map | `Meta/AI/Project-Autoload-Map.md` |

---

## 📈 วัดผล

| Metric | Target |
|--------|--------|
| เวลาเลือกสกิล | < 2 วินาที |
| ความแม่นยำ | > 85% |
| โทเคนที่ใช้ | < 2000/session |
| ไม่ต้องถาม user | > 90% ของกรณี |

---

## 🎓 สรุป

ระบบนี้ทำให้ AI ทุกตัวที่คุณใช้ (Claude Code, Cursor, Windsurf, Gemini, Antigravity) สามารถ:

1. **เข้าถึง 1,390 สกิล** จาก Obsidian vault โดยอัตโนมัติ
2. **เลือกสกิลที่เหมาะสม** โดยไม่ต้องให้ user บอก
3. **ประหยัดโทเคน 50-70%** โดยโหลดแค่ที่จำเป็น
4. **ทำงานได้ทันที** หลังพูด "ใช้สกิล" หรือเริ่ม task

**ผลลัพธ์:** คุณภาพงานดีขึ้น + เร็วขึ้น + ใช้โทเคนน้อยลง

---

## 🔗 Connections
- [[Agent-Adapters]]
- [[Project-Autoload-Map]]
- [[Token-Budget-Tracker]]
- [[Discovery-Roots]]
- [[skills-router|Skills Router]]
