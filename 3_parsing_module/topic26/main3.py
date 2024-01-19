import json

import requests

base_url = 'https://reqres.in'
login_url = base_url + '/api/login'

email = "justcode@reqres.in"
password = "qwerty123"

payload = {'email': email, 'password': password}

response = requests.post(login_url, data=payload)

data = response.json()

print(data)


token = ""
url = ""

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
}

response = requests.get(url, headers=headers)
