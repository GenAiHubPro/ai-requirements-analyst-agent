from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

# llm = ChatOllama(
#     model="gemma4:e2b",
#     temperature=0
# )

# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0
# )

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)