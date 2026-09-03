from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain.tools import tool

import json


@tool
def search_weather(city: str) -> str:
    '''
        Tool that searches over the internet
        Args:
            city: The city we need to check weather in.
        Returns:
            search_result
    '''

    print(f"Searching for weather in the city {city}")
    print(f"It's always sunny in {city}")


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
    