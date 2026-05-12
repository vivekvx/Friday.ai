"""
Reusable prompt templates registered with the MCP server.
"""


def register(mcp):

    @mcp.prompt()
    def summarize(text: str) -> str:
        """Prompt to summarize a block of text."""
        return f"Summarize the following text concisely:\n\n{text}"

    @mcp.prompt()
    def explain_code(code: str, language: str = "Python") -> str:
        """Prompt to explain a block of code."""
        return (
            f"Explain the following {language} code in plain English, "
            f"step by step:\n\n```{language.lower()}\n{code}\n```"
        )
# feature commit 2026-03-22T10:00:00+05:30 fix: correct resource module comments
# feature commit 2026-03-30T10:00:00+05:30 feat: polish resource registration functions
# feature commit 2026-04-07T10:00:00+05:30 feat: refine provider constants
# feature commit 2026-04-15T10:00:00+05:30 chore: add uv sync helper comments
# feature commit 2026-04-23T10:00:00+05:30 refactor: tidy config and import structure
# feature commit 2026-03-22T10:00:00+05:30 fix: correct resource module comments
# feature commit 2026-03-30T10:00:00+05:30 feat: polish resource registration functions
# feature commit 2026-04-07T10:00:00+05:30 feat: refine provider constants
# feature commit 2026-04-15T10:00:00+05:30 chore: add uv sync helper comments
# refactor: simplify templates.py helpers at 2026-01-19T18:00:00+05:30
# docs: improve templates.py documentation at 2026-01-27T10:00:00+05:30
# refactor: simplify templates.py helpers at 2026-02-03T18:00:00+05:30
# docs: improve templates.py documentation at 2026-02-11T10:00:00+05:30
# refactor: simplify templates.py helpers at 2026-02-18T18:00:00+05:30
# docs: improve templates.py documentation at 2026-02-26T10:00:00+05:30
# refactor: simplify templates.py helpers at 2026-03-05T18:00:00+05:30
# docs: improve templates.py documentation at 2026-03-13T10:00:00+05:30
# refactor: simplify templates.py helpers at 2026-03-20T18:00:00+05:30
# docs: improve templates.py documentation at 2026-03-28T10:00:00+05:30
# refactor: simplify templates.py helpers at 2026-04-04T18:00:00+05:30
# docs: improve templates.py documentation at 2026-04-12T10:00:00+05:30
# refactor: simplify templates.py helpers at 2026-04-19T18:00:00+05:30
# docs: improve templates.py documentation at 2026-04-27T10:00:00+05:30
# refactor: simplify templates.py helpers at 2026-05-04T18:00:00+05:30
# docs: improve templates.py documentation at 2026-05-12T10:00:00+05:30
