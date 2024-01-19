import json
import requests
#
base_url = 'https://reqres.in'
login_url = base_url + '/api/login'

payload = {
    "email": "eve.holt@reqres.in",
    "password": "cdc"
}

response = requests.post(login_url, data=payload)

print(f"url: {response.request.url}")
print(f"data: {response.request.body}\n")

result = json.loads(response.text)
result_json = json.dumps(result, indent=4)

print(f"result: {result_json}")

TOKEN = result['token']
print(TOKEN)