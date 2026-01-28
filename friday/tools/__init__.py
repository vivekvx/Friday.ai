"""
Tool registry — imports and registers all tool modules with the MCP server.
Add new tool modules here as you build them.
"""

from friday.tools import web, system, utils


def register_all_tools(mcp):
    """Register all tool groups onto the MCP server instance."""
    web.register(mcp)
    system.register(mcp)
    utils.register(mcp)
# feature commit 2026-03-19T10:00:00+05:30 feat: extend prompt module comments
# feature commit 2026-03-27T10:00:00+05:30 refactor: tidy friday resources exports
# feature commit 2026-04-04T10:00:00+05:30 chore: polish voice agent wiring
# feature commit 2026-04-12T10:00:00+05:30 feat: refine voice provider selection
# feature commit 2026-04-20T10:00:00+05:30 fix: update environment example defaults
# feature commit 2026-04-28T10:00:00+05:30 chore: add code structure polish
# feature commit 2026-03-19T10:00:00+05:30 feat: extend prompt module comments
# feature commit 2026-03-27T10:00:00+05:30 refactor: tidy friday resources exports
# feature commit 2026-04-04T10:00:00+05:30 chore: polish voice agent wiring
# feature commit 2026-04-12T10:00:00+05:30 feat: refine voice provider selection
# fix: update __init__.py details at 2026-01-21T10:00:00+05:30
# fix: correct __init__.py comments at 2026-01-28T18:00:00+05:30
