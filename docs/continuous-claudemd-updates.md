# continuous-claudemd-updates

A comprehensive skill for automatically maintaining CLAUDE.md documentation in sync with codebase changes.

## Purpose

Keeps CLAUDE.md synchronized with codebase changes through automatic analysis after commits and periodic audits. Maintains conciseness by moving detailed content to docs/ folder, removes outdated information, and ensures documentation accuracy.

## Features

- **Automatic change analysis** - Analyzes git commits and determines documentation impact (minor/moderate/major)
- **Conciseness enforcement** - Keeps CLAUDE.md lean by moving verbose content to docs/ folder with proper linking
- **Staleness detection** - Identifies broken file references and outdated configuration mentions
- **Audit capabilities** - Comprehensive documentation quality checks with detailed reports
- **Auto-commit functionality** - Commits CLAUDE.md updates with descriptive messages

## Components

### Scripts

#### `scripts/analyze_changes.py`
Git diff analysis and impact assessment (181 lines)

**Usage**:
```bash
python scripts/analyze_changes.py --commit HEAD
```

**Output**: JSON with change analysis
```json
{
  "commit": "HEAD",
  "commit_message": "Add new feature...",
  "magnitude": {
    "files_changed": 5,
    "insertions": 150,
    "deletions": 20,
    "total_changes": 170
  },
  "categories": {
    "source": ["src/app.ts", "src/utils.ts"],
    "config": ["package.json"]
  },
  "impact": "moderate"
}
```

**Features**:
- Categorizes changed files (config, source, tests, docs, assets)
- Calculates change magnitude with actual line counts (using git --numstat)
- Determines impact level: minor (<30 changes), moderate (30-100), major (>100)
- Provides commit context for decision making

#### `scripts/audit_claudemd.py`
CLAUDE.md validation and issue detection (206 lines)

**Usage**:
```bash
# Generate detailed report
python scripts/audit_claudemd.py --claudemd CLAUDE.md --report

# Output as JSON
python scripts/audit_claudemd.py --claudemd CLAUDE.md --json
```

**Checks**:
- **Missing files**: References to deleted files
- **Untracked files**: References to files not in git
- **Config check**: Outdated configuration mentions
- **Verbosity**: Sections that should be moved to docs/
- **Broken links**: Invalid docs/ links

**Exit codes**:
- `0`: No issues found
- `1`: Issues found (safe for CI/CD integration)

### References

#### `references/guidelines.md`
Content quality standards and best practices

**Topics covered**:
- When to include in CLAUDE.md vs move to docs/
- Content quality standards (concise, current, specific)
- Section organization patterns
- Maintenance workflow
- Red flags to watch for

#### `references/examples.md`
Good vs bad documentation examples

**Examples for**:
- Configuration changes
- Component patterns
- API conventions
- Testing requirements
- Major refactoring scenarios
- When to create docs/ notes

### Assets

#### `assets/note-template.md`
Template for creating detailed docs/ notes

**Structure**:
- Purpose statement
- Overview
- Detailed sections with examples
- Common patterns
- Troubleshooting
- Last updated date

## Triggering Conditions

The skill activates when:

1. **After commit** - A commit has been made and CLAUDE.md needs updating
2. **Explicit request** - User asks for CLAUDE.md update or audit
3. **Major changes** - Refactoring or architectural changes occur
4. **New patterns** - New conventions or patterns are established
5. **File operations** - Files referenced in CLAUDE.md are deleted/moved

## Workflows

### Automatic Mode (After Each Commit)

1. **Analyze changes**
   ```bash
   python scripts/analyze_changes.py --commit HEAD
   ```

2. **Review relevance**
   - Update if: config changed, new patterns, architecture modified, referenced files changed
   - Skip if: only tests changed, minor bug fixes, impact level "minor"

3. **Read current CLAUDE.md**
   ```bash
   cat CLAUDE.md
   ```

4. **Compare and update**
   - Keep entries concise (1-4 sentences)
   - Move verbose content (>3 paragraphs) to docs/
   - Remove outdated information
   - Update file paths that changed

5. **Verify links**
   ```bash
   python scripts/audit_claudemd.py --claudemd CLAUDE.md
   ```

6. **Auto-commit**
   ```bash
   git add CLAUDE.md docs/
   git commit -m "Update CLAUDE.md: [description]"
   ```

### Manual Audit Mode

1. **Run full audit**
   ```bash
   python scripts/audit_claudemd.py --claudemd CLAUDE.md --report
   ```

2. **Review issues** by category:
   - missing_file: Remove or update references
   - untracked_file: Add to git or remove reference
   - config_check: Verify accuracy
   - verbosity: Move to docs/
   - broken_link: Fix or create missing doc

3. **Systematic cleanup**
   - Fix file references
   - Verify configs
   - Reduce verbosity
   - Repair links

4. **Overall coherence check**
   - Structure: logical organization
   - Content: valuable and accurate
   - Completeness: critical info included

5. **Commit audit changes**

## Content Guidelines

### Be Concise
- Use bullet points over paragraphs
- Prefer examples over explanations
- Remove redundant information
- Assume AI agents are competent

### Be Current
- Remove outdated information immediately after changes
- Update references when files are renamed/moved
- Verify configuration references match actual state
- Delete obsolete workflows or patterns

### Be Specific
- Link to actual file paths when referencing code
- Use concrete examples rather than abstract descriptions
- Include exact command syntax for important operations
- Reference specific line numbers for critical patterns

### When to Split to docs/

Move content to docs/ when:
- Information exceeds 3-4 paragraphs
- Content includes extensive code examples (>20 lines)
- Details are reference material rather than procedural
- Information is domain-specific deep-dive
- Content will rarely be needed but should be available

## Installation

### Recommended: Using npx skills (Easiest)

Install directly from GitHub:
```bash
npx skills add vijaykpatel/favorite_skills_and_plugins@continuous-claudemd-updates
```

This automatically:
- Installs to all configured agents (Claude Code, Cursor, etc.)
- Creates proper symlinks
- Handles updates

### Alternative: Manual symlink from favorite_skills_and_plugins

1. Clone the repository:
   ```bash
   cd ~/Developer/favorite_skills_and_plugins
   ```

2. Symlink to Claude skills directory:
   ```bash
   ln -s ~/Developer/favorite_skills_and_plugins/skills/continuous-claudemd-updates ~/.claude/skills/continuous-claudemd-updates
   ```

3. Restart Claude Code or reload skills

### Alternative: Standalone copy

Copy the skill directory to your Claude skills folder:
```bash
cp -r continuous-claudemd-updates ~/.claude/skills/
```

## Usage Examples

### Example 1: After adding a new feature

```bash
# Analyze the commit
python scripts/analyze_changes.py --commit HEAD

# Output shows moderate impact
# Update CLAUDE.md with concise entry:
## New Feature: User Authentication

Using NextAuth.js with session-based auth. Config in `pages/api/auth/[...nextauth].ts`.

See [docs/authentication.md](docs/authentication.md) for setup details.

# Commit the update
git add CLAUDE.md docs/authentication.md
git commit -m "Update CLAUDE.md: Document authentication feature"
```

### Example 2: Configuration change

```bash
# After updating package.json
python scripts/analyze_changes.py --commit HEAD

# Impact: moderate (config changed)
# Update CLAUDE.md:
## Build Scripts

- `npm run dev` - Development server
- `npm run build` - Production build
- `npm run test` - Run test suite (new)

# Commit
git commit -am "Update CLAUDE.md: Add test script documentation"
```

### Example 3: Periodic audit

```bash
# Run audit
python scripts/audit_claudemd.py --report

# Output:
# CONFIG_CHECK (2 issues):
#   • Review package.json references for accuracy
#   • Review tsconfig.json references for accuracy
# VERBOSITY (1 issue):
#   • Consider breaking up long paragraph (542 chars) or moving to docs/

# Fix issues and commit
git commit -am "Audit and update CLAUDE.md"
```

## Integration

### Post-commit Hook

Create `.git/hooks/post-commit`:
```bash
#!/bin/bash
cd /path/to/repo
python scripts/analyze_changes.py --commit HEAD > /tmp/claude-analysis.json

# Check if CLAUDE.md update needed
# (Add your logic here)
```

### CI/CD

```yaml
# .github/workflows/audit-claudemd.yml
name: Audit CLAUDE.md

on: [pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run CLAUDE.md audit
        run: |
          python scripts/audit_claudemd.py --report
```

## Best Practices

1. **Review before committing** - Always check the generated updates
2. **Keep it concise** - If you write >3 paragraphs, move to docs/
3. **Link generously** - Point to docs/ rather than include everything
4. **Remove ruthlessly** - Delete outdated info immediately
5. **Verify links** - Run audit before committing

## Troubleshooting

### Script fails with "git: command not found"
Ensure git is installed and in your PATH.

### Analysis shows wrong impact level
Check that git --numstat output is being parsed correctly. Binary files should be handled as 0 changes.

### Audit reports false positives
Review the file reference regex patterns in `extract_file_references()` function.

## Version

- **Version**: 1.0.0
- **Last Updated**: 2026-01-31
- **Status**: Active

## Related Skills

- **skill-creator** - For creating new skills
- **using-git-worktrees** - For isolated development workflows

## License

MIT License - See repository LICENSE file for details.
