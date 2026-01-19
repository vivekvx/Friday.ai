"""
MCP Prompts — reusable prompt templates exposed to the client.
"""

from friday.prompts import templates


def register_all_prompts(mcp):
    templates.register(mcp)
# docs: document __init__.py workflow at 2026-01-19T10:00:00+05:30
