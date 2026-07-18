# Copyright (C) 2026 Jagadeeswara Rao Patta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Local filesystem document source (single responsibility: local file I/O)."""

import os

from docx import Document
from pypdf import PdfReader

from core.abstractions import DocumentSource

# Input directory is anchored to the project root so it resolves from any CWD.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LocalDocumentSource(DocumentSource):
    def __init__(self, input_dir: str = "input"):
        self._input_dir = (
            input_dir if os.path.isabs(input_dir) else os.path.join(PROJECT_ROOT, input_dir)
        )

    async def get_content(self, file_name: str) -> str:
        target = os.path.join(self._input_dir, file_name)
        if not os.path.exists(target):
            raise FileNotFoundError(
                f"Requirement document not found: {target}\n"
                f"Place the file under the '{os.path.basename(self._input_dir)}' directory."
            )

        ext = os.path.splitext(target)[1].lower()
        if ext == ".docx":
            doc = Document(target)
            return "\n".join(p.text for p in doc.paragraphs)
        if ext == ".pdf":
            reader = PdfReader(target)
            return "\n".join(page.extract_text() or "" for page in reader.pages)
        if ext == ".txt":
            with open(target, "r", encoding="utf-8") as f:
                return f.read()

        raise ValueError(f"Unsupported file type: {ext}")
