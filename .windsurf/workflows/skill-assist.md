---
description: Auto-load relevant skills based on task description using Smart Token Intelligence
triggers: ['use skill', 'use skills', 'skill help', 'need skill', 'ใช้สกิล']
---

# Skill Assist Workflow

**Trigger:** User says "use skill", "skill help", or describes a task

## Steps

1. **Analyze User Intent**
   - Parse task description
   - Identify keywords and context
   - Determine complexity level

2. **Search Relevant Skills**
   ```bash
   vault smart-load "{{user_task}}"
   ```
   // turbo: true

3. **Select Top Skills (STI)**
   - Score by relevance (quality-first)
   - Select 1-3 most relevant
   - Prioritize specific over generic

4. **Load and Apply Skills**
   - Read SKILL.md files
   - Apply to current task
   - Follow skill guidance

5. **Execute with Skill**
   - Use skill patterns
   - Apply best practices
   - Follow skill workflow

## Examples

### Task: "Test API endpoint"
**Selected Skills:**
1. `tdd-workflow` (95% relevance)
2. `backend-patterns` (85% relevance)
3. `api-design` (70% relevance)

**Token Usage:** ~1,200 vs 3,000 traditional (60% savings)

### Task: "Refactor messy code"
**Selected Skills:**
1. `refactor-clean` (98% relevance)
2. `code-review` (82% relevance)

**Quality Boost:** +40% via multi-perspective analysis

## Quality-First Token Strategy

```
User Request → STI Analysis → Precision Loading → Execution
                    ↓
            ┌───────┴───────┐
            ▼               ▼
    Task Complexity    Context Match
            │               │
            └───────┬───────┘
                    ▼
            Load 1-3 Skills
            (Quality Optimized)
                    ↓
            Multi-Perspective
            (Dev + Architect + Security)
                    ↓
            Execution with
            Skill Guidance
```

---

🔗 **Auto-Generated Links**

- [[Work]] - name_mentioned
- [[Task]] - name_mentioned
- [[architect]] - name_mentioned
- [[scribe]] - name_mentioned
- [[SKILL]] - name_mentioned

📅 Auto-linked: 2026-04-28 18:31
