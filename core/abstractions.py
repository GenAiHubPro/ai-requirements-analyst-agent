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

from abc import ABC, abstractmethod

from langchain_core.language_models import BaseChatModel


class DocumentSource(ABC):
    """Abstraction over where requirement documents are read from (ISP/DIP)."""

    @abstractmethod
    async def get_content(self, file_name: str) -> str:
        ...


class ArtifactWriter(ABC):
    """Abstraction over where generated artifacts are persisted (ISP/DIP)."""

    @abstractmethod
    async def write(self, file_path: str, content: str) -> str:
        ...
