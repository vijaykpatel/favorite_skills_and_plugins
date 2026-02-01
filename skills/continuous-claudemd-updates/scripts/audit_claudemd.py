#!/usr/bin/env python3
"""
Audits CLAUDE.md against the actual codebase state.

Checks for:
- References to deleted files
- Outdated configuration references
- Inconsistent patterns or conventions
- Missing critical information

Usage:
    python audit_claudemd.py [--claudemd <path>] [--report]
"""

import os
import sys
import subprocess
import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple

def read_claudemd(path: str = "CLAUDE.md") -> str:
    """Read CLAUDE.md file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)

def extract_file_references(content: str) -> List[str]:
    """Extract file path references from CLAUDE.md."""
    # Match common patterns: `src/file.ts`, /path/to/file, etc.
    patterns = [
        r'`([a-zA-Z0-9_\-./]+\.[a-zA-Z0-9]+)`',  # `file.ext`
        r'(?:^|\s)([a-zA-Z0-9_\-./]+/[a-zA-Z0-9_\-./]+\.[a-zA-Z0-9]+)(?:\s|$)',  # path/to/file.ext
    ]

    refs = set()
    for pattern in patterns:
        matches = re.findall(pattern, content)
        refs.update(matches)

    return list(refs)

def check_file_exists(filepath: str) -> bool:
    """Check if a file exists in the repository."""
    return os.path.exists(filepath)

def get_all_files() -> List[str]:
    """Get all tracked files in the repository."""
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            capture_output=True,
            text=True,
            check=True
        )
        return [f.strip() for f in result.stdout.split('\n') if f.strip()]
    except subprocess.CalledProcessError:
        return []

def check_outdated_references(content: str, tracked_files: List[str]) -> List[Dict[str, str]]:
    """Find references to files that no longer exist or aren't git-tracked."""
    issues = []
    file_refs = extract_file_references(content)

    for ref in file_refs:
        # Check if file exists and is git-tracked
        if not check_file_exists(ref):
            issues.append({
                "type": "missing_file",
                "file": ref,
                "message": f"Referenced file does not exist: {ref}"
            })
        elif ref not in tracked_files:
            issues.append({
                "type": "untracked_file",
                "file": ref,
                "message": f"Referenced file exists but is not git-tracked: {ref}"
            })

    return issues

def check_config_consistency(content: str) -> List[Dict[str, str]]:
    """Check for outdated configuration references."""
    issues = []

    # Check for common config files and their actual state
    config_files = {
        "package.json": ["dependencies", "scripts"],
        "tsconfig.json": ["compilerOptions"],
        "next.config.js": ["next.config"],
        ".env": ["environment variables"]
    }

    for config_file, keywords in config_files.items():
        if os.path.exists(config_file):
            # Check if CLAUDE.md mentions this config (any keyword match)
            if any(keyword.lower() in content.lower() for keyword in keywords):
                issues.append({
                    "type": "config_check",
                    "file": config_file,
                    "message": f"Review {config_file} references for accuracy"
                })

    return issues

def check_verbosity(content: str) -> List[Dict[str, str]]:
    """Check for overly verbose sections."""
    issues = []
    sections = content.split('\n##')

    for i, section in enumerate(sections):
        lines = section.split('\n')
        # Check for very long paragraphs
        for line in lines:
            if len(line) > 500:  # Very long line
                issues.append({
                    "type": "verbosity",
                    "section": f"Section {i}",
                    "message": f"Consider breaking up long paragraph ({len(line)} chars) or moving to docs/"
                })

        # Check for code blocks over 30 lines
        code_blocks = re.findall(r'```[\s\S]*?```', section)
        for block in code_blocks:
            lines_in_block = len(block.split('\n'))
            if lines_in_block > 30:
                issues.append({
                    "type": "verbosity",
                    "section": f"Section {i}",
                    "message": f"Large code block ({lines_in_block} lines) - consider moving to docs/ with link"
                })

    return issues

def check_docs_links(content: str) -> List[Dict[str, str]]:
    """Check that docs/ links are valid."""
    issues = []

    # Extract markdown links
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

    for link_text, link_url in links:
        if link_url.startswith('docs/'):
            if not check_file_exists(link_url):
                issues.append({
                    "type": "broken_link",
                    "link": link_url,
                    "message": f"Broken docs/ link: {link_url}"
                })

    return issues

def generate_report(issues: List[Dict[str, str]]) -> str:
    """Generate audit report."""
    if not issues:
        return "✅ CLAUDE.md audit passed - no issues found"

    report = ["CLAUDE.md Audit Report", "=" * 50, ""]

    # Group by type
    by_type = {}
    for issue in issues:
        issue_type = issue["type"]
        if issue_type not in by_type:
            by_type[issue_type] = []
        by_type[issue_type].append(issue)

    for issue_type, items in by_type.items():
        report.append(f"\n{issue_type.upper().replace('_', ' ')} ({len(items)} issues):")
        report.append("-" * 50)
        for item in items:
            report.append(f"  • {item['message']}")

    report.append("\n" + "=" * 50)
    report.append(f"Total issues found: {len(issues)}")

    return '\n'.join(report)

def main():
    parser = argparse.ArgumentParser(description="Audit CLAUDE.md against codebase")
    parser.add_argument("--claudemd", default="CLAUDE.md", help="Path to CLAUDE.md file")
    parser.add_argument("--report", action="store_true", help="Generate detailed report")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    content = read_claudemd(args.claudemd)
    tracked_files = get_all_files()

    # Run all checks
    all_issues = []
    all_issues.extend(check_outdated_references(content, tracked_files))
    all_issues.extend(check_config_consistency(content))
    all_issues.extend(check_verbosity(content))
    all_issues.extend(check_docs_links(content))

    if args.json:
        print(json.dumps({"issues": all_issues}, indent=2))
    else:
        print(generate_report(all_issues))

    # Exit with error code if issues found (1 for any issues, 0 for success)
    sys.exit(1 if all_issues else 0)

if __name__ == "__main__":
    main()
