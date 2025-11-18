import os
from typing import Literal
from tavily import TavilyClient

# Ensure .env is loaded and environment variables are validated
from . import config  # noqa: F401  (imported for side effects)

# Initialize Tavily client with API key from environment
tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search using Tavily.

    This function will be exposed to the Deep Agent as a tool.
    """
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )
