import asyncio

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()


llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

async def main():
    print("Hello from langchain_client.py!")

if __name__ == "__main__":
    asyncio.run(main())


