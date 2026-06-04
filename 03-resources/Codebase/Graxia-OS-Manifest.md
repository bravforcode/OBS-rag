# Graxia OS Manifest
---
tags: #manifest #architecture #graxia-os
created: 2026-04-26

## 🏗️ System Architecture Overview
Graxia OS is a Sovereign Multi-Agent System (MAS) designed to serve as a bridge between high-level intelligence (Obsidian Brain) and low-level execution (Backend/Integrations).

### 🖥️ Frontend (Next.js/React)
- **Path:** `C:\Users\menum\graxia os\frontend`
- **Source:** `C:\Users\menum\graxia os\frontend\src`
- **Description:** A modern, high-performance web interface for managing agents, tasks, and system status.
- **Key Files:**
  - `C:\Users\menum\graxia os\frontend\package.json` - Dependencies and scripts.
  - `C:\Users\menum\graxia os\frontend\vite.config.ts` - Build configuration.

### ⚙️ Backend (FastAPI)
- **Path:** `C:\Users\menum\graxia os\backend`
- **Application Logic:** `C:\Users\menum\graxia os\backend\app`
- **Description:** Async Python backend using FastAPI, providing the core API and agent orchestration.
- **Key Files:**
  - `C:\Users\menum\graxia os\backend\main.py` - Entry point.
  - `C:\Users\menum\graxia os\backend\requirements.txt` - Python dependencies.
  - `C:\Users\menum\graxia os\backend\app\database.py` - Database connection and session management.

### 🤖 Multi-Agent System (MAS)
- **Path:** `C:\Users\menum\graxia os\backend\app\agents`
- **Central MOC:** [[MAS-War-Room]]
- **Agents:**
  - `C:\Users\menum\graxia os\backend\app\agents\obsidian_sync.py` - Synchronizes data between the system and the Obsidian vault.
  - `C:\Users\menum\graxia os\backend\app\agents\orchestrator.py` - Coordinates multi-agent tasks.
  - `C:\Users\menum\graxia os\backend\app\agents\war_room.py` - High-level decision monitoring.

### 📊 Database & Memory
- **Database Path:** `C:\Users\menum\graxia os\backend\verify_mas_local.db` (SQLite for local MAS state)
- **Migrations:** `C:\Users\menum\graxia os\backend\alembic`
- **Knowledge Library:** [[AI-Master-MOC]]

## 🔗 Project Connections
- **Project Folder:** [[MAS-War-Room|MAS War Room]]
- **Resources:** [[Graxia-OS-Manifest|Manifest]]
- **Inbox:** [[00-inbox/Index|00-Inbox]]
