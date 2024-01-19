
import json
import requests

base_url = 'https://reqres.in'
list_users_url = base_url + '/api/users'

payload = {
    "page": 2
}

token = 'QpwL5tke4Pnpja7X4'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}

response = requests.get(list_users_url, params=payload, headers=headers)

print(response.request.url)

result = json.loads(response.text)
result = json.dumps(result, indent=4)

print(f"result: {result}")

