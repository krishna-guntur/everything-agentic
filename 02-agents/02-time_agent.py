import os
from dotenv import load_dotenv
load_dotenv(r"W:\codebase\everything-agentic\.env")

from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from libtad import TimeService
from libtad.datatypes.places import LocationId


@tool
def get_current_time(country: str, city: str) -> dict :

    """
    Always use this tool to get current time in any geographical location.

    Args:
        country: takes in the country name, lowercase
        city: takes in the city name, lowercase
        
    Returns:
        returns a dict with all the values for date, time and year etc.

    The input to LocationID() should be a country/city.
    Example - for city 'Brisbane', the input to LocationID() should be 'australia/brisbane'

    """

    access_key = os.environ.get("TD_ACCESS_KEY")
    secret_key = os.environ.get("TD_SECRET_KEY")
    
    place = LocationId(f'{country}/{city}')
    service = TimeService(access_key, secret_key)
    service.include_list_of_time_changes = True
    service.include_timezone_information = True

    result = service.current_time_for_place(place)

    return result

def main():

    model = ChatOllama( 
        model="mistral:7b",
        temperature=0
    )

    tools = [get_current_time]

    agent = create_agent(
        model=model,
        tools=tools
    )

    response = agent.invoke({"messages": HumanMessage(input("Enter your query: "))})
    print(response)
    
if __name__ == "__main__":
    main()