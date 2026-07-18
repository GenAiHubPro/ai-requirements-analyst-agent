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

from typing import Callable

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import BaseChatModel
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

# Provider registry: adding a new provider = one entry, no edits elsewhere (OCP).
PROVIDER_REGISTRY: dict[str, Callable[..., BaseChatModel]] = {
    "ollama": lambda model: ChatOllama(model=model, temperature=0),
    "google": lambda model: ChatGoogleGenerativeAI(model=model, temperature=0),
    "groq": lambda model: ChatGroq(model=model, temperature=0),
    "anthropic": lambda model: ChatAnthropic(model_name=model, temperature=0),
}


def get_llm_config(provider: str, model: str) -> BaseChatModel:
    factory = PROVIDER_REGISTRY.get(provider)
    if factory is None:
        raise ValueError(
            f"Unknown MODEL_PROVIDER '{provider}'. "
            f"Available: {', '.join(PROVIDER_REGISTRY)}"
        )
    return factory(model)
