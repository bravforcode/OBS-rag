#!/usr/bin/env python3
"""
Graph Query Tool — Quick access to graphify knowledge graph
Agents use this to understand vault structure before starting tasks.

Usage: python graph-query.py "<question>"
       python graph-query.py --nodes           # list all nodes
       python graph-query.py --edges <node>    # show connections for a node
       python graph-query.py --search <term>   # search nodes by name
       python graph-query.py --clusters        # show community clusters
"""

import json
import sys
from pathlib import Path
from collections import Counter

GRAPH_PATH = Path(__file__).parent.parent.parent / "graphify-out" / "graph.json"


def load_graph():
    with open(GRAPH_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def list_nodes(graph, limit=50):
    """List all nodes grouped by type."""
    nodes = graph.get("nodes", [])
    by_type = {}
    for n in nodes:
        t = n.get("type", "unknown")
        by_type.setdefault(t, []).append(n.get("label", n.get("id", "?")))

    print(f"Total nodes: {len(nodes)}\n")
    for t, labels in sorted(by_type.items()):
        print(f"{t.upper()} ({len(labels)}):")
        for l in labels[:10]:
            print(f"  - {l}")
        if len(labels) > 10:
            print(f"  ... +{len(labels)-10} more")
        print()


def show_connections(graph, node_name):
    """Show all connections for a node."""
    nodes = graph.get("nodes", [])
    edges = graph.get("links", graph.get("edges", []))

    # Find node
    target = None
    for n in nodes:
        if node_name.lower() in n.get("label", "").lower() or node_name.lower() in n.get("id", "").lower():
            target = n
            break

    if not target:
        print(f"Node '{node_name}' not found")
        return

    print(f"Node: {target.get('label', target.get('id'))}")
    print(f"Type: {target.get('type', 'unknown')}")
    print()

    # Find connections
    connected = []
    for e in edges:
        if e.get("source") == target.get("id"):
            for n in nodes:
                if n.get("id") == e.get("target"):
                    connected.append(("OUT", n.get("label", n.get("id")), e.get("relation", "")))
        elif e.get("target") == target.get("id"):
            for n in nodes:
                if n.get("id") == e.get("source"):
                    connected.append(("IN", n.get("label", n.get("id")), e.get("relation", "")))

    print(f"Connections: {len(connected)}")
    for direction, label, relation in sorted(connected, key=lambda x: x[0]):
        arrow = "→" if direction == "OUT" else "←"
        print(f"  {arrow} {label} ({relation})")


def search_nodes(graph, term):
    """Search nodes by name."""
    nodes = graph.get("nodes", [])
    matches = [n for n in nodes if term.lower() in n.get("label", "").lower() or term.lower() in n.get("id", "").lower()]

    print(f"Search: '{term}' — {len(matches)} matches\n")
    for n in matches[:20]:
        print(f"  [{n.get('type', '?')}] {n.get('label', n.get('id'))}")


def show_clusters(graph):
    """Show community clusters."""
    nodes = graph.get("nodes", [])
    edges = graph.get("links", graph.get("edges", []))

    # Simple clustering by type
    by_type = {}
    for n in nodes:
        t = n.get("type", "unknown")
        by_type.setdefault(t, [])
        by_type[t].append(n.get("label", n.get("id")))

    print("Community Clusters:\n")
    for t, labels in sorted(by_type.items(), key=lambda x: -len(x[1])):
        print(f"  {t.upper()}: {len(labels)} nodes")
        for l in labels[:5]:
            print(f"    - {l}")
        if len(labels) > 5:
            print(f"    ... +{len(labels)-5} more")
        print()


def quick_summary(graph):
    """Print quick summary of the graph."""
    nodes = graph.get("nodes", [])
    edges = graph.get("links", graph.get("edges", []))

    by_type = Counter(n.get("type", "unknown") for n in nodes)

    print("=== SECOND BRAIN KNOWLEDGE GRAPH ===\n")
    print(f"Total nodes: {len(nodes)}")
    print(f"Total edges: {len(edges)}")
    print()
    print("By type:")
    for t, count in by_type.most_common():
        print(f"  {t}: {count}")
    print()
    print("Top connected nodes:")
    edge_count = Counter()
    for e in edges:
        edge_count[e.get("source", "")] += 1
        edge_count[e.get("target", "")] += 1
    for nid, count in edge_count.most_common(10):
        for n in nodes:
            if n.get("id") == nid:
                print(f"  {n.get('label', nid)}: {count} connections")
                break


if __name__ == "__main__":
    if not GRAPH_PATH.exists():
        print(f"Graph not found at {GRAPH_PATH}")
        print("Run graphify first.")
        sys.exit(1)

    graph = load_graph()

    if len(sys.argv) < 2:
        quick_summary(graph)
    elif sys.argv[1] == "--nodes":
        list_nodes(graph)
    elif sys.argv[1] == "--edges" and len(sys.argv) > 2:
        show_connections(graph, sys.argv[2])
    elif sys.argv[1] == "--search" and len(sys.argv) > 2:
        search_nodes(graph, sys.argv[2])
    elif sys.argv[1] == "--clusters":
        show_clusters(graph)
    else:
        # Treat as search query
        search_nodes(graph, " ".join(sys.argv[1:]))
