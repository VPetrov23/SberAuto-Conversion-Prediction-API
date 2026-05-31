import requests
import json

with open('sample_request.json', 'r') as file:
    data = json.load(file)


response = requests.post(
    'http://127.0.0.1:8000/predict',
    json=data
)
print(response.json())