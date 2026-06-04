---
type: security-audit
generated: '2026-06-04'
---

# Security Audit Report

Generated: 2026-06-04

## Summary

| Metric | Value |
|--------|-------|
| Files scanned | 6522 |
| Issues found | 1230 |

## Issues by Type

### API_KEY (176 found)

- `brain\github-skills\canopy-readme.md` line 91: `export PINECONE_API_KEY="<PINECONE_API_KEY>"`
- `brain\github-skills\canopy-readme.md` line 92: `export OPENAI_API_KEY="<OPENAI_API_KEY>"`
- `brain\github-skills\composio-readme.md` line 49: `// apiKey: 'your-api-key',`
- `brain\github-skills\composio-readme.md` line 101: `# api_key="your-api-key",`
- `brain\github-skills\crawl4ai-readme.md` line 502: `# provider="ollama/qwen2", api_token="no-token",`
- *... and 171 more*

### AWS_KEY (2 found)

- `brain\skills-archive\engineering-advanced-skills\terraform-patterns\scripts\tf_security_scanner.py` line 28: `access_key = "AKIAIOSFODNN7EXAMPLE"`
- `system\AI\Skills\tf_security_scanner.py` line 28: `access_key = "AKIAIOSFODNN7EXAMPLE"`

### EMAIL (207 found)

- `.obsidian\plugins\dataview\manifest.json` line 7: `"author": "Michael Brenan <blacksmithgu@gmail.com>",`
- `brain\github-skills\ChatDev-readme.md` line 410: `If you have any questions, feedback, or would like to get in touch, please feel `
- `brain\github-skills\composio-readme.md` line 261: `- Contact our [support team](mailto:support@composio.dev)`
- `brain\github-skills\dify-readme.md` line 134: `We provide additional enterprise-centric features. [Send us an email](mailto:bus`
- `brain\github-skills\dify-readme.md` line 239: `To protect your privacy, please avoid posting security issues on GitHub. Instead`
- *... and 202 more*

### ENV_VAR (17 found)

- `brain\github-skills\gpt-researcher-readme.md` line 207: `GOOGLE_API_KEY=your_google_api_key`
- `brain\skills-universal\claude-api\curl\examples.md` line 8: `export ANTHROPIC_API_KEY="your-api-key"`
- `brain\skills-universal\claude-api\curl\managed-agents.md` line 8: `export ANTHROPIC_API_KEY="your-api-key"`
- `brain\skills-universal\graxia-zero-setup\SKILL.md` line 229: `export ANTHROPIC_API_KEY=sk-...   # Now uses Claude instead of Ollama`
- `brain\skills-universal-master\claude-api\curl\examples.md` line 8: `export ANTHROPIC_API_KEY="your-api-key"`
- *... and 12 more*

### HARDCODED_PATH (72 found)

- `.ai\scripts\auto-harvester.py` line 6: `VAULT_ROOT = Path(r"C:\Users\menum\OneDrive\Documents\Gracia")`
- `.ai\scripts\auto-harvester.py` line 8: `HARVEST_DIR = Path(r"C:\Users\menum\graxia os\backend\scripts\harvested_scripts"`
- `.ai\scripts\autonomous-loop.py` line 10: `VAULT_PATH = r"C:\Users\menum\OneDrive\Documents\Gracia"`
- `.ai\scripts\autonomous-loop.py` line 104: `cwd = r"C:\Users\menum\graxia os"`
- `.ai\scripts\backup-verify.py` line 5: `VAULT_PATH = r"C:\Users\menum\OneDrive\Documents\Gracia"`
- *... and 67 more*

### IP_ADDRESS (263 found)

- `.obsidian\plugins\obsidian-local-rest-api\data.json` line 12: `"host":  "127.0.0.1"`
- `01-projects\backend\delta\20260417T004755.json` line 12: `"cd \"c:\\brav os/backend\" && python -m uvicorn app.main:app --host 127.0.0.1 -`
- `01-projects\backend\delta\20260417T004755.json` line 13: `"ping -n 8 127.0.0.1 > /dev/null 2>&1 && curl -s http://127.0.0.1:8000/health 2>`
- `01-projects\backend\delta\20260417T004755.json` line 16: `"curl -s http://127.0.0.1:8000/health | python -m json.tool 2>/dev/null && echo `
- `01-projects\backend\delta\20260417T045539.json` line 6: `"curl -s -X POST http://127.0.0.1:8000/api/v1/auth/login -H \"Content-Type: appl`
- *... and 258 more*

### PHONE (484 found)

- `.obsidian\graph.json` line 13: `"nodeSizeMultiplier": 1.02193347193347,`
- `.obsidian\graph.json` line 16: `"centerStrength": 0.504158004158004,`
- `.obsidian\graph.json` line 20: `"scale": 0.05295182241220177,`
- `.obsidian-mobile\graph.json` line 13: `"nodeSizeMultiplier": 1.02193347193347,`
- `.obsidian-mobile\graph.json` line 16: `"centerStrength": 0.504158004158004,`
- *... and 479 more*

### PRIVATE_KEY (9 found)

- `.obsidian\plugins\obsidian-local-rest-api\data.json` line 9: `"privateKey":  "-----BEGIN RSA PRIVATE KEY-----\r\nMIIEowIBAAKCAQEAlbKPJjnUJQzoi`
- `brain\skills-archive\engineering-advanced-skills\skill-tester\tests\test_security_scorer.py` line 118: `code = 'private_key = "-----BEGIN RSA PRIVATE KEY-----"'`
- `brain\skills-archive\engineering-advanced-skills\skill-tester\tests\test_security_scorer.py` line 274: `private_key = "-----BEGIN RSA PRIVATE KEY-----MIIEowIBAAJCA..."`
- `brain\skills-archive\engineering-skills\senior-security\scripts\secret_scanner.py` line 165: `regex=r'-----BEGIN RSA PRIVATE KEY-----',`
- `brain\skills-archive\engineering-skills\senior-security\scripts\secret_scanner.py` line 174: `regex=r'-----BEGIN EC PRIVATE KEY-----',`
- *... and 4 more*

## Risk Assessment

- **Critical**: 11 (private keys, AWS keys, GitHub tokens)
- **High**: 193 (API keys, env vars)
- **Medium**: 72 (hardcoded paths)
- **Low**: 954 (emails, phones, IPs)

**Action Required**: Review critical and high severity issues.

---
*Report generated by security-audit.py*
