import os
import asyncio
from dotenv import load_dotenv

load_dotenv()


print(os.getenv("GEMINI_API_KEY"))

async def main():
    print("Hello from mcp-server-test!")


if __name__ == "__main__":
    asyncio.run(main())
