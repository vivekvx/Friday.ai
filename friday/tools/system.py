"""
System tools — time, environment info, shell commands, etc.
"""

import datetime
import platform


def register(mcp):

    @mcp.tool()
    def get_current_time() -> str:
        """Return the current date and time in ISO 8601 format."""
        return datetime.datetime.now().isoformat()

    @mcp.tool()
    def get_system_info() -> dict:
        """Return basic information about the host system."""
        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "python_version": platform.python_version(),
        }
# refactor: tidy system.py layout at 2026-01-21T18:00:00+05:30
# docs: document system.py workflow at 2026-01-29T10:00:00+05:30
# refactor: tidy system.py layout at 2026-02-05T18:00:00+05:30
# docs: document system.py workflow at 2026-02-13T10:00:00+05:30
# refactor: tidy system.py layout at 2026-02-20T18:00:00+05:30
# docs: document system.py workflow at 2026-02-28T10:00:00+05:30
# refactor: tidy system.py layout at 2026-03-07T18:00:00+05:30
