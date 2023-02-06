import requests

endpoint = "http://localhost:8000/api/products/21251251253"


get_response = requests.get(endpoint)

print(get_response.json())