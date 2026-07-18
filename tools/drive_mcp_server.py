# Copyright (C) 2026 Jagadeeswara Rao Patta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Google Drive MCP server (single responsibility: expose Drive tools only)."""

import os
import sys

# Make the project root importable when run directly from any directory,
# so `import bootstrap` and the `tools.*` / `core.*` packages resolve.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bootstrap  # noqa: F401  (ensures project root is importable from any CWD)

from fastmcp import FastMCP

from tools.drive_auth import load_credentials
from tools.drive_source import DriveDocumentSource

mcp = FastMCP("GoogleDriveMCP")

_drive_source = DriveDocumentSource(load_credentials("token.json"))


@mcp.tool()
def list_files():
    """Get list of all available files in my drive."""
    import asyncio

    return asyncio.run(_drive_source.list_files())


@mcp.tool()
def get_file_content(file_name: str) -> str:
    """Search a file by name in Google Drive and return its text content."""
    import asyncio

    try:
        return asyncio.run(_drive_source.get_content(file_name))
    except FileNotFoundError as exc:
        return str(exc)


if __name__ == "__main__":
    mcp.run(transport="http")
