import requests

headers = {'Authorization': 'Bearer afe244a1c5f40d540be58d84712f59a57ce1564b'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done"
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
