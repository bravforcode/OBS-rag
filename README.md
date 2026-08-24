# OBS-RAG — Obsidian Second-Brain RAG Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![RAG](https://img.shields.io/badge/RAG-Hybrid_Retrieval-7c3aed?style=for-the-badge)
![Obsidian](https://img.shields.io/badge/Obsidian-Second_Brain-7C3AED?style=for-the-badge&logo=obsidian&logoColor=white)

> **Ask your notes anything.** RAG pipeline over Obsidian vaults — hybrid retrieval (BM25 + dense + reranking) for personal knowledge.

### Demo

> 🎬 **Demo coming soon** — screen capture will be added at `docs/demo.gif`

### Architecture

```mermaid
graph LR
  A[Obsidian Vault] --> B[Markdown Parser]
  B --> C[Chunker + Embedder]
  C --> D[(Vector Store)]
  Q[User Query] --> E[Hybrid Retrieval: BM25 + Dense]
  E --> F[Reranker]
  F --> G[LLM Answer + Citations]
```

### Results

| Metric | Value |
|---|---|
| **Retrieval** | Hybrid BM25 + dense + rerank |
| **Source** | Obsidian markdown vaults |


---

**Phirawit Jitnarong — Strategic Full-Stack & AI Engineer**

xme176@gmail.com · 092-551-0427 · [LinkedIn](https://www.linkedin.com/in/%E0%B8%9E%E0%B8%B5%E0%B8%A3%E0%B8%A7%E0%B8%B4%E0%B8%8A%E0%B8%8D%E0%B9%8C-%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B8%93%E0%B8%A3%E0%B8%87%E0%B8%84%E0%B9%8C-0000393a4) · [Fastwork](https://fastwork.co/user/bravforcode?source=search)

> Hiring for this stack? Let's talk — production hardened, 300k+ users shipped.