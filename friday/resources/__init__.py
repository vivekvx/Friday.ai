"""
MCP Resources — expose static or dynamic data to the client.
"""

from friday.resources import data


def register_all_resources(mcp):
    data.register(mcp)
# chore: finalize __init__.py notes at 2026-01-20T10:00:00+05:30
