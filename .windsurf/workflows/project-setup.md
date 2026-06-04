---
description: Setup new project with appropriate templates - FastAPI, React, or ML
triggers: ['new project', 'create project', 'setup project', 'เริ่มโปรเจกต์', 'สร้างโปรเจกต์']
---

# Project Setup Workflow

**Trigger:** User wants to create new project

## Steps

1. **Determine Project Type**
   - Ask: "Backend (FastAPI), Frontend (React), or ML?"
   - Or detect from context

2. **Select Template**
   - Backend → [[fastapi-project]]
   - Frontend → [[react-vite-template]]
   - ML → [[ml-project]]

3. **Gather Project Details**
   - Project name
   - Location
   - Specific requirements

4. **Apply Template**
   ```bash
   # Copy template structure
   mkdir {{project_name}}
   cp -r brain/templates/{{template}}/* {{project_name}}/
   
   # Customize with project name
   find {{project_name}} -type f -exec sed -i 's/my-project/{{project_name}}/g' {} \;
   ```
   // turbo: true

5. **Setup Dependencies**
   ```bash
   cd {{project_name}}
   
   # Python projects
   python scripts/setup.py
   
   # Node projects
   npm install
   ```
   // turbo: true

6. **Initialize Git**
   ```bash
   git init
   git add .
   git commit -m "Initial commit from template"
   ```
   // turbo: true

7. **Install Git Hooks**
   ```bash
   .\brain\git-hooks\install-hooks.ps1
   ```
   // turbo: true

8. **Verify Setup**
   - Run tests
   - Check build
   - Verify dev server

## Output

- **Project created** with full structure
- **Dependencies installed**
- **Git initialized** with hooks
- **Ready to develop**

## Post-Setup

1. Add project to [[Project-Autoload-Map]]
2. Create initial MOC entry
3. Set up CI/CD (optional)
4. Deploy first version (optional)

## Example Interaction

**User:** "สร้างโปรเจกต์ API ใหม่ชื่อ my-api"

**AI:** 
```
🎯 Setting up FastAPI project: my-api

✅ Template applied
✅ Dependencies installed  
✅ Git initialized
✅ Hooks installed

Next steps:
1. cd my-api
2. docker-compose up -d
3. Start coding in app/main.py

Use 'ใช้สกิล' anytime for guidance!
```
