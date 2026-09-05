from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from tavily import TavilyClient


import json

tavily = TavilyClient()

@tool
def search_weather(query: str) -> str:
    '''
        Tool that searches over the internet
        Args:
            query: The query that needs to be searched on the internet.
        Returns:
            search_result
    '''

    print("Using Tavily Client")
    tavily.search(query=query)


def main():

    mistral_model = ChatOllama(
        model="mistral:7b",
        temperature=0
    )

    agent = create_agent(
        model=mistral_model,
        tools=[search_weather]
    )

    response = agent.invoke({"messages": HumanMessage(input("Enter your query: "))})
    
    with open(r'.\02-agents\response.json', 'a') as file:
        json.dump(response, file, indent=4, default=str)


if __name__ == "__main__":
    main()
    