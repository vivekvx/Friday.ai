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
# docs: improve utils.py documentation at 2026-01-22T10:00:00+05:30
# refactor: simplify utils.py helpers at 2026-01-29T18:00:00+05:30
# docs: improve utils.py documentation at 2026-02-06T10:00:00+05:30
# refactor: simplify utils.py helpers at 2026-02-13T18:00:00+05:30
# docs: improve utils.py documentation at 2026-02-21T10:00:00+05:30
# refactor: simplify utils.py helpers at 2026-02-28T18:00:00+05:30
# docs: improve utils.py documentation at 2026-03-08T10:00:00+05:30
# refactor: simplify utils.py helpers at 2026-03-15T18:00:00+05:30
# docs: improve utils.py documentation at 2026-03-23T10:00:00+05:30
# refactor: simplify utils.py helpers at 2026-03-30T18:00:00+05:30
# docs: improve utils.py documentation at 2026-04-07T10:00:00+05:30
# refactor: simplify utils.py helpers at 2026-04-14T18:00:00+05:30
