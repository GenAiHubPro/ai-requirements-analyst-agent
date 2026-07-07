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

from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm_config(provider: str, model: str):
    match provider:
        case "ollama":
            return ChatOllama(
                model=model,
                temperature=0
            )
        case "google":
            return ChatGoogleGenerativeAI(
                model=model,
                temperature=0
            )
        case "groq":
            return ChatGroq(
                model=model,
                temperature=0,
            )
        case "anthropic":
            return ChatAnthropic(
                model_name=model,
                temperature=0,
            )
        case _:
            return None



