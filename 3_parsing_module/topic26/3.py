import json
import requests

base_url = 'https://reqres.in'
list_users_url = base_url + '/api/users'

payload = {
    "page": 3
}

response = requests.get(list_users_url, params=payload)

print(response.request.url)

result = json.loads(response.text)
result = json.dumps(result, indent=4)

print(f"result: {result}")

