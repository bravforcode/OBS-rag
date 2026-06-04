#!/usr/bin/env python3
"""
Run Graphify Pipeline — Second Brain
Runs the full graphify pipeline on the vault.

Usage: python run-graphify.py
"""

import os
import sys
import json
import subprocess
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
GRAPHIFY_OUT = VAULT_ROOT / "graphify-out"


def run_graphify():
    """Run the full graphify pipeline."""
    os.chdir(VAULT_ROOT)
    GRAPHIFY_OUT.mkdir(exist_ok=True)

    print("=" * 60)
    print("GRAPHIFY PIPELINE — Second Brain")
    print("=" * 60)

    # Step 1: Detect
    print("\n[1/5] Detecting files...")
    try:
        from graphify.detect import detect
        result = detect(Path("."))
        total = result.get("total_files", 0)
        words = result.get("total_words", 0)
        code = len(result.get("files", {}).get("code", []))
        print(f"  Corpus: {total} files, ~{words} words, {code} code files")
    except Exception as e:
        print(f"  Detect error: {e}")
        return

    # Step 2: Extract
    print("\n[2/5] Extracting knowledge graph...")
    try:
        from graphify.extract import extract
        from graphify.config import default_config
        config = default_config()
        graph = extract(Path("."), config=config)
        print(f"  Nodes: {len(graph.get('nodes', []))}")
        print(f"  Edges: {len(graph.get('edges', []))}")
    except Exception as e:
        print(f"  Extract error: {e}")
        print("  Trying alternative approach...")
        try:
            # Try with simpler config
            from graphify.pipeline import pipeline
            graph = pipeline(Path("."), output_dir=GRAPHIFY_OUT)
            print(f"  Pipeline completed")
        except Exception as e2:
            print(f"  Pipeline error: {e2}")
            return

    # Step 3: Cluster
    print("\n[3/5] Running community detection...")
    try:
        from graphify.cluster import cluster
        clustered = cluster(graph)
        communities = clustered.get("communities", [])
        print(f"  Communities found: {len(communities)}")
    except Exception as e:
        print(f"  Cluster error: {e}")

    # Step 4: Generate report
    print("\n[4/5] Generating report...")
    try:
        from graphify.report import generate_report
        report = generate_report(graph)
        report_path = GRAPHIFY_OUT / "GRAPH_REPORT.md"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"  Report: {report_path}")
    except Exception as e:
        print(f"  Report error: {e}")

    # Step 5: Generate visualization
    print("\n[5/5] Generating visualization...")
    try:
        from graphify.visualize import generate_html
        html_path = GRAPHIFY_OUT / "graph.html"
        generate_html(graph, output_path=html_path)
        print(f"  HTML: {html_path}")
    except Exception as e:
        print(f"  Visualization error: {e}")

    # Save graph JSON
    graph_json_path = GRAPHIFY_OUT / "graph.json"
    with open(graph_json_path, "w", encoding="utf-8") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False, default=str)
    print(f"  JSON: {graph_json_path}")

    print("\n" + "=" * 60)
    print("GRAPHIFY COMPLETE!")
    print("=" * 60)
    print(f"\nOutputs in: {GRAPHIFY_OUT}/")
    print(f"  - graph.html (interactive visualization)")
    print(f"  - graph.json (GraphRAG-ready)")
    print(f"  - GRAPH_REPORT.md (plain-language report)")
    print(f"\nOpen graph.html in browser to explore!")


if __name__ == "__main__":
    run_graphify()
