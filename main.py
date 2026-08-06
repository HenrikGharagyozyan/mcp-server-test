import asyncio
import traceback

from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)

server_params = StdioServerParameters(
    command="python",
    args=["/home/henrik/Projects/mcp-server-test/servers/math_server.py"],
)


async def main():
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("Session initialized")

                tools = await load_mcp_tools(session)

                print("Available tools:")
                for tool in tools:
                    print(f" - {tool.name}")

                agent = create_agent(
                    model=llm,
                    tools=tools,
                )

                print("Invoking agent...")

                result = await agent.ainvoke(
                    {
                        "messages": [
                            HumanMessage(
                                content="What is 54 + 2 * 3?"
                            )
                        ]
                    }
                )

                print("\n=== Final Answer ===")
                print(result["messages"][-1].content)

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())