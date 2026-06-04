---
status: unprocessed
project: unknown
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:55.702734'
---

type: {{type}}
date: "{{YYYY-MM-DD}}"
tags: [{{tag1}}, {{tag2}}]
status: {{status}}
---
```

**Valid status values**:
- `inbox` — recently created, not yet filed
- `draft` — work in progress
- `active` — current project or ongoing
- `completed` — finished, work done
- `archived` — no longer relevant

## Linting & Auto-Format

The Obsidian Linter plugin (recommended) can auto-enforce many of these rules:
- Title Case for note titles
- YAML frontmatter consistency
- Proper spacing and formatting
- Trailing spaces removed

Configuration: See `.obsidian/plugins/linter/` (auto-generated after plugin install).

## Exceptions & Special Cases

### Thai Language Notes
- File names remain in English (for filesystem compatibility), tags describe language
- Content can be in Thai: `บันทึกวิจัย — Research Note Title`
- Use tag: `#language/thai` to mark Thai-language notes
- Example: `Research Note — สิ่งที่ฉันเรียนรู้` (What I Learned)

### Long Titles
- If a title exceeds 80 characters, consider breaking into title + subtitle with em-dash:
  - ✓ `Thesis Chapter 3 — Methodology & Research Design`
  - ✗ `Thesis Chapter 3 Methodology Research Design And Implications`

### Non-English Filenames
- Keep filenames ASCII for filesystem compatibility
- Content is fully multilingual (English, Thai, etc.)
- Use descriptive English filenames + language tags in YAML

---

## Updates to These Rules

If naming conventions change:

1. Update this file
2. Update `Meta/agent-log.md` to record the change
3. Architect or Librarian may batch-rename affected notes
4. New notes follow updated rules automatically

**Last Updated**: 2026-04-06 (Architect, onboarding)

## 🔗 Semantic Connections
- [[tag-taxonomy]]
- [[vault-structure]]
- [[agent-log]]
