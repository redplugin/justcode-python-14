import requests

base_url = 'https://reqres.in'
get_users_url = base_url + '/api/users'

payload = {'page': 2}

response = requests.get(get_users_url, params=payload)

data = response.json()

print(data)

