# Favorite Skills and Plugins

A curated collection of agent skills and plugins for enhancing Claude Code and other AI agents.

## Structure

```
favorite_skills_and_plugins/
├── skills/          # Claude Code skills and agent capabilities
├── plugins/         # MCP servers and plugin integrations
├── examples/        # Example configurations and usage patterns
├── docs/           # Documentation and guides
└── .github/        # GitHub Actions and repository automation
```

## Skills

The `skills/` directory contains reusable agent skills that extend Claude Code's capabilities. Each skill is typically defined in a `SKILL.md` file with instructions, triggers, and workflows.

### Available Skills

| Skill Name | Source |
|------------|--------|
| Vercel React Best Practices | [skills.sh](https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices) |

### Usage

To use a skill:
1. Copy the skill directory to your `~/.claude/skills/` folder
2. Restart Claude Code or reload skills
3. Invoke with the appropriate trigger phrase or slash command

## Plugins

The `plugins/` directory contains MCP (Model Context Protocol) servers and other plugin integrations that provide tools and resources to agents.

### Available Plugins

| Plugin Name | Source |
|-------------|--------|
| *No plugins yet* | - |

### Usage

To use a plugin:
1. Follow the installation instructions in the plugin's README
2. Configure in your `~/.claude/config.json` or MCP settings
3. Access via the plugin's provided tools

## Getting Started

1. Clone this repository:
   ```bash
   git clone <repo-url> favorite_skills_and_plugins
   cd favorite_skills_and_plugins
   ```

2. Browse available skills and plugins
3. Follow individual installation instructions
4. Customize for your workflow

## Contributing

Add your own skills and plugins:
1. Create a new directory in `skills/` or `plugins/`
2. Include a README.md with usage instructions
3. Document dependencies and configuration
4. Commit and push changes

## License

MIT License - See LICENSE file for details
