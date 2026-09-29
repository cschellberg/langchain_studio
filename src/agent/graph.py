"""Simple demo agent for LangGraph Studio.

A minimal ReAct-style agent: a chat model that can call one tool
(a fake weather lookup) and reply to the user.
"""

from __future__ import annotations

from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent


def get_weather(city: str) -> str:
    """Look up the current weather for a city."""
    return f"It's always sunny in {city}!"


graph = create_react_agent(
    model=ChatAnthropic(model="claude-sonnet-5"),
    tools=[get_weather],
    prompt="You are a helpful assistant.",
    name="Demo Agent",
)
