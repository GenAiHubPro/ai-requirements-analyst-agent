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

"""Local filesystem artifact writer (single responsibility: persistence only)."""

import os
import sys

# Make the project root importable when this module is loaded directly.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bootstrap  # noqa: F401  (ensures project root is importable from any CWD)

from core.abstractions import ArtifactWriter

# Project root is the parent of the `tools` package so artifacts always land
# in <project>/output regardless of the current working directory.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LocalArtifactWriter(ArtifactWriter):
    def __init__(self, base_dir: str = "output", execution_id: str | None = None):
        # Anchor relative base_dir to the project root, not the CWD.
        self._base_dir = (
            base_dir if os.path.isabs(base_dir) else os.path.join(PROJECT_ROOT, base_dir)
        )
        # Each execution gets its own subfolder under base_dir.
        self._execution_id = execution_id

    async def write(self, file_path: str, content: str) -> str:
        # Scope artifacts to the execution folder when an id is provided.
        rel_path = (
            os.path.join(self._execution_id, file_path) if self._execution_id else file_path
        )
        target = os.path.join(self._base_dir, rel_path)
        parent = os.path.dirname(os.path.abspath(target))
        os.makedirs(parent, exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully created artifact at: {target}"
