from dotenv import load_dotenv
import os
from browser_use import Agent
import logging
import asyncio
from langchain_openai.chat_models import ChatOpenAI
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
async def main():
    try:
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),

        )
        logger.info("ChatOpenAI init successfully")
        agent = Agent(
            task="Go to baidu, search for 'browser-use' in the search bar, extract the titles of the first ten search results.",
            llm=llm,
        )
        result = await agent.run()
        print(result)

    except Exception as e:
        logger.error(f" ChatOpenAI fail: {e}")
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"program fail : {e}")
