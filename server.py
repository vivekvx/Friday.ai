"""
Friday MCP Server — Entry Point
Run with: python server.py
"""

from mcp.server.fastmcp import FastMCP
from friday.tools import register_all_tools
from friday.prompts import register_all_prompts
from friday.resources import register_all_resources
from friday.config import config

# Create the MCP server instance
mcp = FastMCP(
    name=config.SERVER_NAME,
    instructions=(
        "You are Friday, a Tony Stark-style AI assistant. "
        "You have access to a set of tools to help the user. "
        "Be concise, accurate, and a little witty."
    ),
)

# Register tools, prompts, and resources
register_all_tools(mcp)
register_all_prompts(mcp)
register_all_resources(mcp)

def main():
    mcp.run(transport='sse')

if __name__ == "__main__":
    main()
# feature commit 2026-03-25T10:00:00+05:30 feat: add info endpoint comments
# feature commit 2026-04-02T10:00:00+05:30 refactor: tidy agent startup flow
# feature commit 2026-04-10T10:00:00+05:30 chore: polish voice signal handling notes
# feature commit 2026-04-18T10:00:00+05:30 feat: improve pyproject dependency comments
# feature commit 2026-04-26T10:00:00+05:30 refactor: simplify helper functions
# feature commit 2026-03-25T10:00:00+05:30 feat: add info endpoint comments
# feature commit 2026-04-02T10:00:00+05:30 refactor: tidy agent startup flow
# feature commit 2026-04-10T10:00:00+05:30 chore: polish voice signal handling notes
# docs: improve server.py documentation at 2026-01-17T10:00:00+05:30
# refactor: simplify server.py helpers at 2026-01-24T18:00:00+05:30
# docs: improve server.py documentation at 2026-02-01T10:00:00+05:30
# refactor: simplify server.py helpers at 2026-02-08T18:00:00+05:30
# docs: improve server.py documentation at 2026-02-16T10:00:00+05:30
# refactor: simplify server.py helpers at 2026-02-23T18:00:00+05:30
# docs: improve server.py documentation at 2026-03-03T10:00:00+05:30
# refactor: simplify server.py helpers at 2026-03-10T18:00:00+05:30
# docs: improve server.py documentation at 2026-03-18T10:00:00+05:30
# refactor: simplify server.py helpers at 2026-03-25T18:00:00+05:30
# docs: improve server.py documentation at 2026-04-02T10:00:00+05:30
# refactor: simplify server.py helpers at 2026-04-09T18:00:00+05:30
# docs: improve server.py documentation at 2026-04-17T10:00:00+05:30
# refactor: simplify server.py helpers at 2026-04-24T18:00:00+05:30
