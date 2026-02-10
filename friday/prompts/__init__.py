"""
MCP Prompts — reusable prompt templates exposed to the client.
"""

from friday.prompts import templates


def register_all_prompts(mcp):
    templates.register(mcp)
# docs: document __init__.py workflow at 2026-01-19T10:00:00+05:30
# refactor: tidy __init__.py layout at 2026-01-26T18:00:00+05:30
# docs: document __init__.py workflow at 2026-02-03T10:00:00+05:30
# refactor: tidy __init__.py layout at 2026-02-10T18:00:00+05:30
