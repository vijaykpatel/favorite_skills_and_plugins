#!/usr/bin/env python3
"""
Analyzes git changes and determines their impact on CLAUDE.md.

Usage:
    python analyze_changes.py [--commit <hash>] [--branch <branch>]

    --commit: Analyze specific commit (default: HEAD)
    --branch: Compare against branch (default: main)
"""

import subprocess
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

def get_git_diff(commit: str = "HEAD") -> str:
    """Get git diff numstat for the specified commit."""
    try:
        if commit == "HEAD":
            # Compare working directory with last commit
            result = subprocess.run(
                ["git", "diff", "HEAD~1..HEAD", "--numstat"],
                capture_output=True,
                text=True,
                check=True
            )
        else:
            result = subprocess.run(
                ["git", "diff", f"{commit}~1..{commit}", "--numstat"],
                capture_output=True,
                text=True,
                check=True
            )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error getting git diff: {e}", file=sys.stderr)
        return ""

def get_changed_files(commit: str = "HEAD") -> List[str]:
    """Get list of changed files."""
    try:
        if commit == "HEAD":
            result = subprocess.run(
                ["git", "diff", "HEAD~1..HEAD", "--name-only"],
                capture_output=True,
                text=True,
                check=True
            )
        else:
            result = subprocess.run(
                ["git", "diff", f"{commit}~1..{commit}", "--name-only"],
                capture_output=True,
                text=True,
                check=True
            )
        return [f.strip() for f in result.stdout.split('\n') if f.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Error getting changed files: {e}", file=sys.stderr)
        return []

def get_commit_message(commit: str = "HEAD") -> str:
    """Get commit message."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=%B", commit],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting commit message: {e}", file=sys.stderr)
        return ""

def analyze_change_magnitude(diff_stats: str) -> Dict[str, int]:
    """Analyze the magnitude of changes from git diff --numstat output.

    Format: <insertions>\t<deletions>\t<filename>
    Example: 413\t0\tfile.txt
    """
    lines = diff_stats.split('\n')
    total_files = 0
    total_insertions = 0
    total_deletions = 0

    for line in lines:
        if not line.strip():
            continue

        parts = line.split('\t')
        if len(parts) >= 3:
            total_files += 1
            try:
                # Handle binary files (marked as '-')
                insertions = 0 if parts[0] == '-' else int(parts[0])
                deletions = 0 if parts[1] == '-' else int(parts[1])

                total_insertions += insertions
                total_deletions += deletions
            except ValueError:
                # Skip lines that can't be parsed
                continue

    return {
        "files_changed": total_files,
        "insertions": total_insertions,
        "deletions": total_deletions,
        "total_changes": total_insertions + total_deletions
    }

def categorize_files(files: List[str]) -> Dict[str, List[str]]:
    """Categorize changed files by type."""
    categories = {
        "config": [],
        "source": [],
        "tests": [],
        "docs": [],
        "assets": [],
        "other": []
    }

    config_patterns = ['.json', '.yaml', '.yml', '.toml', '.env', 'config']
    test_patterns = ['test', 'spec', '__tests__']
    doc_patterns = ['.md', 'README', 'docs/']
    asset_patterns = ['.png', '.jpg', '.svg', '.css', '.scss']

    for file in files:
        file_lower = file.lower()

        if any(pattern in file_lower for pattern in config_patterns):
            categories["config"].append(file)
        elif any(pattern in file_lower for pattern in test_patterns):
            categories["tests"].append(file)
        elif any(pattern in file_lower for pattern in doc_patterns):
            categories["docs"].append(file)
        elif any(pattern in file_lower for pattern in asset_patterns):
            categories["assets"].append(file)
        elif file.endswith(('.js', '.ts', '.tsx', '.jsx', '.py', '.go', '.rs', '.java')):
            categories["source"].append(file)
        else:
            categories["other"].append(file)

    return {k: v for k, v in categories.items() if v}

def assess_impact(magnitude: Dict[str, int], categories: Dict[str, List[str]]) -> str:
    """Assess the impact level of changes."""
    total_changes = magnitude["total_changes"]
    files_changed = magnitude["files_changed"]

    # Major change indicators
    if total_changes > 100 or files_changed > 10:
        return "major"
    elif "config" in categories and len(categories.get("config", [])) > 2:
        return "major"
    elif total_changes > 30 or files_changed > 3:
        return "moderate"
    else:
        return "minor"

def main():
    parser = argparse.ArgumentParser(description="Analyze git changes for CLAUDE.md updates")
    parser.add_argument("--commit", default="HEAD", help="Commit hash to analyze")

    args = parser.parse_args()

    # Gather change data
    diff_stats = get_git_diff(args.commit)
    changed_files = get_changed_files(args.commit)
    commit_msg = get_commit_message(args.commit)

    # Analyze changes
    magnitude = analyze_change_magnitude(diff_stats)
    categories = categorize_files(changed_files)
    impact = assess_impact(magnitude, categories)

    # Output analysis
    analysis = {
        "commit": args.commit,
        "commit_message": commit_msg,
        "magnitude": magnitude,
        "categories": categories,
        "impact": impact,
        "changed_files": changed_files
    }

    print(json.dumps(analysis, indent=2))

if __name__ == "__main__":
    main()
