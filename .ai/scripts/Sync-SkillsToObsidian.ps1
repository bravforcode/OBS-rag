$ErrorActionPreference = "Stop"

# Obsidian Paths
$vaultBase = "C:\Users\menum\Documents\ObsidianVault\Second Brain\brain"
$localSkillsDir = Join-Path $vaultBase "skills-universal"
$githubSkillsDir = Join-Path $vaultBase "github-skills"
$catalogFile = Join-Path $vaultBase "skills-catalog.md"

# Create directories if they do not exist
if (-not (Test-Path $localSkillsDir)) { New-Item -ItemType Directory -Path $localSkillsDir | Out-Null }
if (-not (Test-Path $githubSkillsDir)) { New-Item -ItemType Directory -Path $githubSkillsDir | Out-Null }

$localSkillsList = @()
$githubSkillsList = @()

# ==========================================
# 1. Sync Local Skills (300+ items)
# ==========================================
Write-Host "[1/3] Copying Local Skills to Obsidian..." -ForegroundColor Cyan
$hermesHome = "$env:LOCALAPPDATA\hermes"
$skillDirs = @(
    "C:\Users\menum\.agents\skills", 
    "C:\Users\menum\.claude\skills",
    "$hermesHome\skills"
)

foreach ($dirPath in $skillDirs) {
    if (Test-Path $dirPath) {
        $subdirs = Get-ChildItem -Path $dirPath -Directory
        foreach ($dir in $subdirs) {
            $skillFile = Join-Path $dir.FullName "SKILL.md"
            if (Test-Path $skillFile) {
                $name = $dir.Name
                $content = Get-Content -Raw $skillFile
                
                # Extract Description for Catalog
                $description = "No description provided."
                if ($content -match '(?s)^---\s*\n(.*?)\n---') {
                    $yaml = $Matches[1]
                    if ($yaml -match '(?m)^description:\s*(.*)') {
                        $description = $Matches[1].Trim(' "')
                    }
                }
                
                # Write to Obsidian Vault
                $obsidianFilePath = Join-Path $localSkillsDir "$name.md"
                $frontmatter = @"
---
tags: [ai-skill, local-skill]
source: local
name: $name
---

"@
                $finalContent = $frontmatter + $content
                [System.IO.File]::WriteAllText($obsidianFilePath, $finalContent, [System.Text.Encoding]::UTF8)
                
                $localSkillsList += [PSCustomObject]@{
                    Name = $name
                    Description = $description
                    Link = "[[skills-universal/$name|$name]]"
                }
            }
        }
    }
}
Write-Host "SUCCESS: Copied $($localSkillsList.Count) local skills." -ForegroundColor Green

# ==========================================
# 2. GitHub Scraper Engine
# ==========================================
Write-Host "`n[2/3] Scraping GitHub Repositories..." -ForegroundColor Cyan

# Target repositories containing AI Skills / Agents
$targetRepos = @(
    # --- CORE MCP & SKILLS ---
    "modelcontextprotocol/servers",         # Official MCP Servers
    "ComposioHQ/composio",                  # Composio AI Skills
    "browserbase/mcp-server-browserbase",   # Browserbase MCP
    "replicate/mcp-server-replicate",       # Replicate MCP
    "get-convex/mcp-server-convex",         # Convex MCP
    "tiny-interliner/mcp-server-duckduckgo",# DuckDuckGo MCP
    "execute-code/mcp-server-shell",        # Shell/Code Execution MCP
    "mcp-get/mcp-get",                      # MCP Package Manager

    # --- TOP AI AGENTS & OS ---
    "Significant-Gravitas/AutoGPT",         # AutoGPT
    "All-Hands-AI/OpenHands",               # OpenHands (OpenDevin)
    "cline/cline",                          # Cline (Autonomous Coding)
    "geekan/MetaGPT",                       # MetaGPT
    "smol-ai/developer",                    # Smol Developer
    "Doriandarko/maestro",                  # Maestro Orchestrator
    "Assafelovic/gpt-researcher",           # GPT Researcher
    "OpenBMB/ChatDev",                      # ChatDev (Virtual Company)
    "Stellar-21/G-Eval",                    # Evaluation Agent
    "TransformerOptimus/SuperAGI",          # SuperAGI
    "Skyvern-AI/skyvern",                   # Web Automation Agent
    "multion-api/multion-python",           # MultiOn Web Agent
    "lavague-ai/LaVague",                   # Large Action Model framework

    # --- LLM FRAMEWORKS & RAG ---
    "langchain-ai/langchain",               # LangChain
    "run-llama/llama_index",                # LlamaIndex
    "microsoft/autogen",                    # AutoGen
    "joaomdmoura/crewAI",                   # CrewAI
    "langgenius/dify",                      # Dify.ai
    "haystack-ai/haystack",                 # Haystack
    "huggingface/transformers",             # Transformers
    "huggingface/diffusers",                # Diffusers
    "huggingface/datasets",                 # Datasets
    "vllm-project/vllm",                    # vLLM Serving
    "THUDM/ChatGLM-6B",                     # ChatGLM
    "mistralai/mistral-src",                # Mistral Official
    "facebookresearch/llama",               # Llama Official
    "ollama/ollama",                        # Ollama (Local LLM)
    "lmstudio-ai/lms-cli",                  # LM Studio CLI
    "chujieyang/facad",                     # Agent Framework
    "openai/openai-python",                 # OpenAI Python SDK

    # --- COOKBOOKS & KNOWLEDGE ---
    "anthropics/anthropic-cookbook",        # Anthropic Cookbook
    "openai/openai-cookbook",               # OpenAI Cookbook
    "GoogleCloudPlatform/generative-ai",    # Google Generative AI
    "aws-samples/amazon-bedrock-workshop",  # AWS Bedrock
    "microsoft/generative-ai-for-beginners",# MS GenAI Course
    "dair-ai/Prompt-Engineering-Guide",     # Prompt Engineering Guide
    "brexhq/prompt-engineering",            # Brex Prompt Engineering

    # --- WEB & DATA EXTRACTION ---
    "mendableai/firecrawl",                 # Firecrawl (Scraping)
    "unclecode/crawl4ai",                   # Crawl4AI
    "adrianhajdin/ai_saas_app",             # AI SaaS Reference
    "steven-tey/novel",                     # Notion-style AI Editor
    "Nutlope/roomGPT",                      # RoomGPT
    "tldraw/tldraw",                        # tldraw (Make Real)

    # --- DATABASE & STORAGE ---
    "pinecone-io/canopy",                   # Pinecone Canopy
    "milvus-io/milvus",                     # Milvus Vector DB
    "qdrant/qdrant",                        # Qdrant Vector DB
    "chroma-core/chroma",                   # Chroma DB
    "weaviate/weaviate",                    # Weaviate

    # --- TOOLS & UTILITIES ---
    "Mintplex-Labs/anything-llm",           # AnythingLLM
    "khoj-ai/khoj",                         # Khoj AI
    "n8n-io/n8n",                           # n8n Automation
    "activepieces/activepieces",            # Open Source Automation
    "make-vfs/vfs",                         # Virtual File System
    "shubham-modi/mcp-github-server",       # GitHub MCP Server
    "markus-wa/mcp-obsidian",               # Obsidian MCP Server
    "ZillizPCP/GPTCache",                   # LLM Caching
    "microsoft/promptflow",                 # Prompt Flow
    "BerriAI/litellm",                      # LiteLLM (Proxy)

    # --- IMAGE & MULTIMEDIA ---
    "AUTOMATIC1111/stable-diffusion-webui", # Stable Diffusion WebUI
    "comfyanonymous/ComfyUI",               # ComfyUI
    "black-forest-labs/flux",               # Flux.1
    "elevenlabs/elevenlabs-python",         # ElevenLabs SDK
    "openai/whisper",                       # Whisper ASR
    "suno-ai/bark"                          # Bark Audio Gen
)

# Load GitHub Token from .env file
$envFile = Join-Path $PSScriptRoot "..\..\.env"
$githubToken = $null
if (Test-Path $envFile) {
    $envContent = Get-Content $envFile
    foreach ($line in $envContent) {
        if ($line -match "^GITHUB_PERSONAL_ACCESS_TOKEN=(.*)") {
            $githubToken = $Matches[1].Trim()
        }
    }
}

function Scrape-GitHubRepo {
    param([string]$repoPath)
    
    $repoName = ($repoPath -split "/")[1]
    Write-Host "   -> Scanning $repoPath ..."
    
    $headers = @{"User-Agent"="Obsidian-Skill-Scraper"}
    if ($githubToken) {
        $headers.Add("Authorization", "token $githubToken")
    }
    
    try {
        # Fetch Main README
        $readmeUrl = "https://api.github.com/repos/$repoPath/readme"
        $response = Invoke-RestMethod -Uri $readmeUrl -Headers $headers
        
        $downloadUrl = $response.download_url
        $readmeContent = Invoke-RestMethod -Uri $downloadUrl
        
        $obsidianFilePath = Join-Path $githubSkillsDir "$repoName-readme.md"
        $frontmatter = @"
---
tags: [ai-skill, github-scrape, mcp]
repo: $repoPath
url: https://github.com/$repoPath
---

# GitHub Repository: $repoPath
*Scraped automatically to serve as an AI Skill Reference.*

"@
        $finalContent = $frontmatter + $readmeContent
        [System.IO.File]::WriteAllText($obsidianFilePath, $finalContent, [System.Text.Encoding]::UTF8)
        
        $script:githubSkillsList += [PSCustomObject]@{
            Name = $repoName
            Description = "Source Code & Docs from https://github.com/$repoPath"
            Link = "[[github-skills/$repoName-readme|$repoName]]"
        }
        Write-Host "      [OK] Downloaded $repoName" -ForegroundColor Green
    } catch {
        Write-Warning "      [Error] Failed to fetch $repoPath ($($_.Exception.Message))"
    }
}

foreach ($repo in $targetRepos) {
    Scrape-GitHubRepo -repoPath $repo
}

# ==========================================
# 3. Build Central Catalog
# ==========================================
Write-Host "`n[3/3] Building Central Catalog (skills-catalog.md)..." -ForegroundColor Cyan
$catalogContent = @"
---
updated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
tags: [index, skills, AI]
---
# AI Skills & Agents Catalog (The Brain)

This catalog is auto-generated as a **Reference Hub** for AI Agents to lookup Source Code and Instructions for skills. (RAG Protocol for token efficiency).

## GitHub Scraped Skills ($($githubSkillsList.Count) Repositories)

| Repository / Name | Description |
|-------------------|-------------|
"@

foreach ($skill in ($githubSkillsList | Sort-Object Name -Unique)) {
    $catalogContent += "`n| $($skill.Link) | $($skill.Description) |"
}

$catalogContent += @"


## Local AI Skills ($($localSkillsList.Count) skills)

| Skill Name | Description |
|------------|-------------|
"@

foreach ($skill in ($localSkillsList | Sort-Object Name -Unique)) {
    # Sanitize description for markdown tables
    $desc = $skill.Description -replace "\|", "\|" -replace "`n", " "
    $catalogContent += "`n| $($skill.Link) | $desc |"
}

[System.IO.File]::WriteAllText($catalogFile, $catalogContent, [System.Text.Encoding]::UTF8)
Write-Host "SUCCESS: Built Skill & Code Hub in Obsidian!" -ForegroundColor Green
Write-Host "   -> Catalog saved to: $catalogFile" -ForegroundColor Yellow
