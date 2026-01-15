"""
Utility tools — text processing, formatting, calculations, etc.
"""

import json


def register(mcp):

    @mcp.tool()
    def format_json(data: str) -> str:
        """Pretty-print a JSON string."""
        try:
            parsed = json.loads(data)
            return json.dumps(parsed, indent=2)
        except json.JSONDecodeError as e:
            return f"Invalid JSON: {e}"

    @mcp.tool()
    def word_count(text: str) -> dict:
        """Count words, characters, and lines in a block of text."""
        lines = text.splitlines()
        words = text.split()
        return {
            "characters": len(text),
            "words": len(words),
            "lines": len(lines),
        }
# feature commit 2026-03-20T10:00:00+05:30 refactor: tidy prompt registration helpers
# feature commit 2026-03-28T10:00:00+05:30 fix: correct resource module comments
# feature commit 2026-04-05T10:00:00+05:30 feat: improve LiveKit agent setup
# feature commit 2026-04-13T10:00:00+05:30 refactor: improve agent lifecycle handling
# feature commit 2026-04-21T10:00:00+05:30 chore: add uv sync helper comments
# feature commit 2026-04-29T10:00:00+05:30 refactor: tidy config and import structure
# feature commit 2026-03-20T10:00:00+05:30 refactor: tidy prompt registration helpers
# feature commit 2026-03-28T10:00:00+05:30 fix: correct resource module comments
# feature commit 2026-04-05T10:00:00+05:30 feat: improve LiveKit agent setup
# feature commit 2026-04-13T10:00:00+05:30 refactor: improve agent lifecycle handling
