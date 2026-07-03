from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".venv"))

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



