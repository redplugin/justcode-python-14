import json

import requests
from requests.auth import HTTPBasicAuth

base_url = 'https://reqres.in'
# reg = base_url + '/api/users?page=1'
reg = base_url + '/api/users'

# email = "eve.holt@reqres.in"
# password = "pistol"

# Set up basic authentication with the provided credentials
# auth = HTTPBasicAuth(email, password)
# payload = {'email': email, 'password': password}
payload = {'page': 2}

# response = requests.post(reg, data=payload)
response = requests.get(reg, params=payload)
# response = requests.get(reg)

data = response.text
data2 = response.json()
# data3 = json.dumps(response.json(), indent=4)
data3 = json.loads(response.text, )

print(data)
print(data2)
print(data3)
print(type(data3))


