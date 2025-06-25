import requests
import json
from headers import *

url = f"https://{host}/last/USD-BRL,EUR-BRL,BTC-BRL"

headers = {
    "x-rapidapi-host": host,
    "x-rapidapi-key": API_KEY
}

response = requests.get(url, headers=headers)
response_json = response.json()

with open('cotacao_data.json', 'w') as f:
    json.dump(response_json, f, indent=4)
    
print("Dados salvos em cotacao_data.json")
