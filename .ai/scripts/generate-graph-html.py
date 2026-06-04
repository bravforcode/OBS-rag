#!/usr/bin/env python3
"""Generate HTML visualization from graph.json"""
import json
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
GRAPH_PATH = VAULT_ROOT / "graphify-out" / "graph.json"
HTML_PATH = VAULT_ROOT / "graphify-out" / "graph.html"

with open(GRAPH_PATH, "r", encoding="utf-8") as f:
    graph = json.load(f)

nodes = graph.get("nodes", [])
edges = graph.get("edges", [])

# Limit for browser performance
nodes_limited = nodes[:300]
edges_limited = [e for e in edges if any(n["id"] == e.get("source") or n["id"] == e.get("target") for n in nodes_limited)][:800]

html = f"""<!DOCTYPE html>
<html>
<head>
<title>Second Brain Knowledge Graph</title>
<style>
body {{ margin: 0; background: #1a1a2e; color: #eee; font-family: system-ui; }}
canvas {{ display: block; }}
.info {{ position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.8); padding: 15px; border-radius: 8px; z-index: 10; }}
.info h2 {{ margin: 0 0 10px 0; color: #e94560; }}
.info p {{ margin: 5px 0; font-size: 14px; }}
.controls {{ position: absolute; top: 10px; right: 10px; background: rgba(0,0,0,0.8); padding: 15px; border-radius: 8px; }}
button {{ background: #e94560; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin: 5px; }}
button:hover {{ background: #c73e54; }}
</style>
</head>
<body>
<div class="info">
<h2>Second Brain Knowledge Graph</h2>
<p>Nodes: {len(nodes)} | Edges: {len(edges)}</p>
<p>Showing: {len(nodes_limited)} nodes, {len(edges_limited)} edges</p>
<p>Generated: 2026-06-04</p>
</div>
<div class="controls">
<button onclick="resetView()">Reset View</button>
<button onclick="toggleLabels()">Toggle Labels</button>
</div>
<canvas id="graph"></canvas>
<script>
const canvas = document.getElementById('graph');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const allNodes = {json.dumps(nodes_limited, default=str)};
const allEdges = {json.dumps(edges_limited, default=str)};

const colors = {{code: '#e94560', doc: '#0f3460', folder: '#16213e', default: '#533483'}};
let showLabels = true;
let scale = 1;
let offsetX = 0, offsetY = 0;
let dragging = null;
let lastMouse = {{x: 0, y: 0}};

// Initialize positions
const cx = canvas.width / 2;
const cy = canvas.height / 2;
allNodes.forEach((n, i) => {{
    const angle = (i / allNodes.length) * Math.PI * 2;
    const r = 200 + Math.random() * 200;
    n.x = cx + Math.cos(angle) * r;
    n.y = cy + Math.sin(angle) * r;
    n.vx = 0; n.vy = 0;
}});

// Force simulation
for (let iter = 0; iter < 80; iter++) {{
    for (let i = 0; i < allNodes.length; i++) {{
        for (let j = i + 1; j < allNodes.length; j++) {{
            let dx = allNodes[j].x - allNodes[i].x;
            let dy = allNodes[j].y - allNodes[i].y;
            let d = Math.sqrt(dx*dx + dy*dy) || 1;
            let f = 300 / (d * d);
            allNodes[i].vx -= dx/d * f;
            allNodes[i].vy -= dy/d * f;
            allNodes[j].vx += dx/d * f;
            allNodes[j].vy += dy/d * f;
        }}
    }}
    allEdges.forEach(e => {{
        let s = allNodes.find(n => n.id === e.source);
        let t = allNodes.find(n => n.id === e.target);
        if (s && t) {{
            let dx = t.x - s.x;
            let dy = t.y - s.y;
            let d = Math.sqrt(dx*dx + dy*dy) || 1;
            let f = (d - 80) * 0.005;
            s.vx += dx/d * f; s.vy += dy/d * f;
            t.vx -= dx/d * f; t.vy -= dy/d * f;
        }}
    }});
    allNodes.forEach(n => {{
        n.vx += (cx - n.x) * 0.0005;
        n.vy += (cy - n.y) * 0.0005;
        n.x += n.vx * 0.1; n.y += n.vy * 0.1;
        n.vx *= 0.9; n.vy *= 0.9;
    }});
}}

function draw() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(offsetX, offsetY);
    ctx.scale(scale, scale);

    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.lineWidth = 0.5;
    allEdges.forEach(e => {{
        let s = allNodes.find(n => n.id === e.source);
        let t = allNodes.find(n => n.id === e.target);
        if (s && t) {{
            ctx.beginPath();
            ctx.moveTo(s.x, s.y);
            ctx.lineTo(t.x, t.y);
            ctx.stroke();
        }}
    }});

    allNodes.forEach(n => {{
        ctx.fillStyle = colors[n.type] || colors.default;
        ctx.beginPath();
        ctx.arc(n.x, n.y, 4, 0, Math.PI * 2);
        ctx.fill();
        if (showLabels && n.label) {{
            ctx.fillStyle = '#aaa';
            ctx.font = '10px system-ui';
            ctx.fillText(n.label, n.x + 6, n.y + 3);
        }}
    }});
    ctx.restore();
    requestAnimationFrame(draw);
}}
draw();

canvas.addEventListener('wheel', e => {{
    e.preventDefault();
    const zoom = e.deltaY > 0 ? 0.9 : 1.1;
    scale *= zoom;
}});

canvas.addEventListener('mousedown', e => {{
    lastMouse = {{x: e.clientX, y: e.clientY}};
}});

canvas.addEventListener('mousemove', e => {{
    offsetX += e.clientX - lastMouse.x;
    offsetY += e.clientY - lastMouse.y;
    lastMouse = {{x: e.clientX, y: e.clientY}};
}});

function resetView() {{ scale = 1; offsetX = 0; offsetY = 0; }}
function toggleLabels() {{ showLabels = !showLabels; }}
</script>
</body>
</html>"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)
print(f"HTML visualization: {HTML_PATH}")
