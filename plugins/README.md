# Plugins

This directory contains MCP servers and plugin integrations for agent workflows.

## Structure

Each plugin should be organized as:

```
plugin-name/
├── README.md          # Installation and usage
├── src/              # Source code
├── package.json      # Dependencies (if Node.js)
└── config/           # Configuration templates
```

## Plugin Types

- **MCP Servers**: Model Context Protocol servers that provide tools and resources
- **Tool Integrations**: Wrappers around external APIs and services
- **Data Providers**: Plugins that supply context or information

## Installing Plugins

1. Navigate to the plugin directory
2. Follow installation instructions in the plugin's README
3. Configure in `~/.claude/config.json` or appropriate config file
4. Restart Claude Code if necessary

## Available Plugins

<!-- List your plugins here as you add them -->

- *No plugins yet - add your first one!*
