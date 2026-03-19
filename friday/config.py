"""
Configuration — load environment variables and app-wide settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Server identity
    SERVER_NAME: str = os.getenv("SERVER_NAME", "Friday")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # External API keys (add as needed)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    SEARCH_API_KEY: str = os.getenv("SEARCH_API_KEY", "")


config = Config()
# feature commit 2026-03-18T10:00:00+05:30 feat: refine prompt templates and exports
# feature commit 2026-03-26T10:00:00+05:30 feat: improve resource metadata docs
# feature commit 2026-04-03T10:00:00+05:30 fix: update voice entrypoint docs
# feature commit 2026-04-11T10:00:00+05:30 feat: wire voice agent to MCP SSE tools
# feature commit 2026-04-19T10:00:00+05:30 refactor: polish package entrypoints
# feature commit 2026-04-27T10:00:00+05:30 fix: update package initialization comments
# feature commit 2026-03-18T10:00:00+05:30 feat: refine prompt templates and exports
# feature commit 2026-03-26T10:00:00+05:30 feat: improve resource metadata docs
# feature commit 2026-04-03T10:00:00+05:30 fix: update voice entrypoint docs
# feature commit 2026-04-11T10:00:00+05:30 feat: wire voice agent to MCP SSE tools
# fix: correct config.py comments at 2026-01-18T18:00:00+05:30
# fix: update config.py details at 2026-01-26T10:00:00+05:30
# fix: correct config.py comments at 2026-02-02T18:00:00+05:30
# fix: update config.py details at 2026-02-10T10:00:00+05:30
# fix: correct config.py comments at 2026-02-17T18:00:00+05:30
# fix: update config.py details at 2026-02-25T10:00:00+05:30
# fix: correct config.py comments at 2026-03-04T18:00:00+05:30
# fix: update config.py details at 2026-03-12T10:00:00+05:30
# fix: correct config.py comments at 2026-03-19T18:00:00+05:30
