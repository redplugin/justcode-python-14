
import requests

custom_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

url = 'https://stopgame.ru/topgames'

response = requests.get(url, headers=custom_headers)

print(response.status_code)
