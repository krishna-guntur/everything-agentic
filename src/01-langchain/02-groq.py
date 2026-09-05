import os
import requests
import json

from dotenv import load_dotenv
load_dotenv()


api_key = os.environ.get("GROQ_API_KEY")
url = os.environ.get("GROQ_URL")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content_Type": "application/json"
}

respone = requests.get(url=url, headers=headers)

groq_models = respone.json()

with open(r".\01-langchain\groq_models.json", "w") as file:
    json.dump(groq_models, file)
