import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

stdio_server_params = StdioServerParameters(
    command = "python", 
    args = ["/home/henrik/Projects/mcp-server-test/servers/math_server.py"],
)

async def main():
    print("Hello from mcp-server-test!")


if __name__ == "__main__":
    asyncio.run(main())
