---
tags:
  - '#api'
  - '#testing'
  - '#task'
auto_classified: true
classified_at: 2026-04-28T18:31:33.603Z
confidence: 1
status: active
---

# เริ่มต้นใช้งาน Smart Skill System

**สร้าง:** 2026-04-28  
**เวอร์ชัน:** 2.0.0  
**สกิลทั้งหมด:** 1,390 สกิล

---

## 🎯 อะไรคือ Smart Skill System?

ระบบที่ทำให้ AI ทุกตัว (Claude Code, Cursor, Windsurf, Gemini, Antigravity, Copilot) สามารถ:
- **Auto-detect** สกิลที่ควรใช้จาก context
- **โหลดอัตโนมัติ** เมื่อพูด "ใช้สกิล" หรือเริ่ม task
- **ประหยัดโทเคน 50-70%** โดยโหลดแค่ที่จำเป็น

---

## 🚀 เริ่มต้นใช้งานใน 1 นาที

### 1. Claude Code (VS Code)

**วิธี A: Global Config (ใช้ทุกโปรเจกต์)**
ไฟล์: `%USERPROFILE%\.claude\CLAUDE.md`
```bash
# สร้าง symbolic link (Windows)
mklink "C:\Users\menum\.claude\CLAUDE.md" "C:\Users\menum\Documents\ObsidianVault\Second Brain\CLAUDE.md"
```

**วิธี B: Project-Specific (แนะนำ)**
ไฟล์นี้อยู่แล้วใน `C:\Users\menum\Documents\ObsidianVault\Second Brain\CLAUDE.md`
คัดลอกไปวางใน root ของแต่ละโปรเจกต์

### 2. Cursor IDE

ไฟล์นี้อยู่แล้ว: `.cursorrules` (ใน Second Brain/)

**ทำในแต่ละโปรเจกต์:**
```bash
# คัดลอกไปยังโปรเจกต์
xcopy "C:\Users\menum\Documents\ObsidianVault\Second Brain\.cursorrules" "C:\your-project\" /Y
```

หรือ **Global Settings:**
- Cursor → Settings → AI Rules
- ใส่ path: `C:\Users\menum\Documents\ObsidianVault\Second Brain\.cursorrules`

### 3. Windsurf (Cascade)

ไฟล์นี้อยู่แล้ว: `.windsurfrules` (ใน Second Brain/)

**ทำในแต่ละโปรเจกต์:**
```bash
xcopy "C:\Users\menum\Documents\ObsidianVault\Second Brain\.windsurfrules" "C:\your-project\" /Y
```

### 4. Gemini (Claude.ai)

**Custom Instructions:**
ไปที่ Settings → Custom Instructions
วางข้อความจากไฟล์:
`C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal\claude-ai-custom-instructions.md`

### 5. Antigravity

ไฟล์นี้อยู่แล้ว: `.antigravity/config.yaml` (ใน Second Brain/)

**คัดลอกไปยังโปรเจกต์:**
```bash
xcopy "C:\Users\menum\Documents\ObsidianVault\Second Brain\.antigravity" "C:\your-project\.antigravity\" /E /Y
```

### 6. GitHub Copilot / Codex

ไฟล์นี้อยู่แล้ว: `.github/copilot-instructions.md` (ใน Second Brain/)

**คัดลอกไปยังโปรเจกต์:**
```bash
xcopy "C:\Users\menum\Documents\ObsidianVault\Second Brain\.github" "C:\your-project\.github\" /E /Y
```

---

## 💡 วิธีใช้งาน

### Trigger Words (พูดอะไรก็ได้)
- "**ใช้สกิล**" / "**use skills**"
- "**โหลดสกิล**" / "**load skills**"
- "**ช่วยด้วย**" + คำบรรยายงาน
- หรือแค่เริ่มทำงาน → AI จะ **auto-detect** เอง

### ตัวอย่างการใช้งาน

```
👤 User: "ช่วยเทส API ให้หน่อย"
🤖 AI: [Auto-load tdd-workflow + backend-patterns]
      "ใช้ TDD workflow นะครับ... เริ่มสร้าง test ก่อน"

👤 User: "refactor โค้ดนี้"
🤖 AI: [Auto-load refactor-clean + code-review]
      "ใช้ clean refactoring patterns..."

👤 User: "deploy ขึ้น production"
🤖 AI: [Auto-load deployment-patterns + security-checklist]
      "ตรวจสอบ security ก่อน deploy..."
```

---

## 🧠 การ Auto-Detect

AI จะตรวจจับ context จาก:

| สัญญาณ | สกิลที่โหลด |
|--------|-------------|
| `.test.ts`, `.spec.py` | tdd-workflow |
| `refactor`, `clean up` | refactor-clean |
| `deploy`, `docker` | deployment-patterns |
| `api`, `endpoint` | backend-patterns |
| `ui`, `component` | frontend-patterns |
| `security`, `auth` | security-review |
| `bug`, `fix` | focused-fix |

---

## 📊 Token Efficiency

| วิธี | โทเคนที่ใช้ |
|------|-------------|
| ก่อนใช้ Smart Loader | 3000-5000 |
| หลังใช้ Smart Loader | 1000-2000 |
| **ประหยัด** | **50-70%** |

---

## 🔧 Files สำคัญ

| ไฟล์ | ที่อยู่ |
|------|---------|
| Smart Loader | `brain/skills-universal/_smart-skill-loader/SKILL.md` |
| Skill Router | `brain/skills-universal/skills-router.md` |
| Registry | `brain/skills-universal/skills-registry-compact.json` |
| คู่มือเต็ม | `Meta/AI/Smart-Skill-System.md` |

---

## ✅ Checklist เริ่มต้น

- [ ] Claude Code: มี CLAUDE.md ในโปรเจกต์
- [ ] Cursor: มี .cursorrules ในโปรเจกต์
- [ ] Windsurf: มี .windsurfrules ในโปรเจกต์
- [ ] Gemini: ตั้งค่า Custom Instructions
- [ ] Antigravity: มี .antigravity/config.yaml
- [ ] Copilot: มี .github/copilot-instructions.md
- [ ] ทดสอบ: พูด "ใช้สกิล" แล้ว AI โหลดสกิล

---

## 🆘 แก้ไขปัญหา

### AI ไม่โหลดสกิล
1. ตรวจสอบว่าไฟล์ config (.cursorrules, .windsurfrules) อยู่ใน root โปรเจกต์
2. ลองพิมพ์ trigger word ชัดเจน: "ใช้สกิล tdd-workflow"
3. ตรวจสอบ path ใน config ว่าถูกต้อง

### Skill ไม่ตรงกับงาน
- AI จะเลือก skill ที่เหมาะสมที่สุด
- ถ้าไม่ตรง ให้บอกชื่อ skill ที่ต้องการ: "ใช้สกิล security-review"

### ใช้โทเคนเยอะเกินไป
- ระบบจะโหลดแค่ 1-3 skills ต่อ session
- ถ้าใช้โทเคนมาก ให้ cache skill ที่ใช้บ่อย

---

**พร้อมใช้งาน!** เริ่มด้วยการพูด "**ใช้สกิล**" ใน AI tool ที่ต้องการ

---

🔗 **Auto-Generated Links**

- [[CLAUDE]] - name_mentioned
- [[copilot-instructions]] - name_mentioned
- [[Work]] - name_mentioned
- [[CLAUDE]] - name_mentioned
- [[Project]] - name_mentioned

📅 Auto-linked: 2026-04-28 18:30
