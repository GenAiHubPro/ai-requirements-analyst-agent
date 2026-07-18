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

from langchain_core.language_models import BaseChatModel
from langchain_ollama import ChatOllama


def get_llm_config(provider: str, model: str) -> BaseChatModel:
    if provider != "ollama":
        raise ValueError(
            f"Unsupported MODEL_PROVIDER '{provider}'. Only 'ollama' is configured."
        )
    return ChatOllama(model=model, temperature=0)
