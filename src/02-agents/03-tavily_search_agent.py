import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch


tools = [TavilySearch()]
model = ChatOllama(
    model='llama3.1:8b',
    temperature=0
)

agent = create_agent(
    model=model,
    tools=tools
)

response = agent.invoke({"messages": HumanMessage("what is the weather today in Beijing?")})

print(response)

