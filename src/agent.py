from deepagents import create_deep_agent

from .search_tools import internet_search

# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research
and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results
to return, the topic, and whether raw content should be included.
"""

# Create the deep agent backed by LangGraph via deepagents
agent = create_deep_agent(
    tools=[internet_search],
    system_prompt=research_instructions,
)
