import json
import requests

base_url = 'https://reqres.in'
list_users_url = base_url + '/api/users?page=1'

response = requests.get(list_users_url)

result = json.loads(response.text)
result_as_json = json.dumps(result, indent=4)

print(f"result: {result_as_json}")

# print(f"{result['data']=}")
# print(f"{result['data'][0]=}")



