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

import logging
from abc import ABC, abstractmethod

from langchain_core.language_models import BaseChatModel

from schemas.state import RequirementState


class BaseAgent(ABC):
    """Formal agent contract so every agent is substitutable (LSP).

    Subclasses implement ``run``. The shared ``__call__`` behavior (logging
    and LLM guard) lives here so no agent re-implements it inconsistently.
    """

    name: str = "BaseAgent"

    def __init__(self, llm: BaseChatModel):
        if llm is None:
            raise ValueError(f"[{self.name}] LLM is not available")
        self.llm = llm

    async def __call__(self, state: RequirementState) -> RequirementState:
        logger = logging.getLogger(self.name)
        logger.info("%s started", self.name)
        state = await self.run(state)
        logger.info("%s finished", self.name)
        return state

    @abstractmethod
    async def run(self, state: RequirementState) -> RequirementState:
        ...
