import requests


response = requests.get('http://localhost:8000/posts/test/')

# print(response.text)
print(response.json())
