"""
Data resources — expose static content or dynamic data via MCP resources.
"""


def register(mcp):

    @mcp.resource("friday://info")
    def server_info() -> str:
        """Returns basic info about this MCP server."""
        return (
            "Friday MCP Server\n"
            "A Tony Stark-inspired AI assistant.\n"
            "Built with FastMCP."
        )
# feature commit 2026-03-23T10:00:00+05:30 chore: add resource integration notes
# feature commit 2026-03-31T10:00:00+05:30 feat: add info endpoint comments
# feature commit 2026-04-08T10:00:00+05:30 fix: update SSE tool comments
# feature commit 2026-04-16T10:00:00+05:30 fix: refine provider guide implementation notes
# feature commit 2026-04-24T10:00:00+05:30 refactor: clean up tool module layout
# feature commit 2026-03-23T10:00:00+05:30 chore: add resource integration notes
# feature commit 2026-03-31T10:00:00+05:30 feat: add info endpoint comments
# feature commit 2026-04-08T10:00:00+05:30 fix: update SSE tool comments
# feature commit 2026-04-16T10:00:00+05:30 fix: refine provider guide implementation notes
# feat: refine data.py structure at 2026-01-20T18:00:00+05:30
# feat: add context to data.py at 2026-01-28T10:00:00+05:30
# feat: refine data.py structure at 2026-02-04T18:00:00+05:30
# feat: add context to data.py at 2026-02-12T10:00:00+05:30
# feat: refine data.py structure at 2026-02-19T18:00:00+05:30
# feat: add context to data.py at 2026-02-27T10:00:00+05:30
# feat: refine data.py structure at 2026-03-06T18:00:00+05:30
# feat: add context to data.py at 2026-03-14T10:00:00+05:30
# feat: refine data.py structure at 2026-03-21T18:00:00+05:30
