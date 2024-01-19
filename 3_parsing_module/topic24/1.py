
import requests
from bs4 import BeautifulSoup

# custom_headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Custom-Header': 'YourCustomValue',
# }

url = 'https://quotes.toscrape.com/'

# response = requests.get(url, headers=custom_headers)
response = requests.get(url)

# for key, value in response.headers.items():
#     print(f"{key}: {value}")
# print("================================================")

data = response.text

soup = BeautifulSoup(data, "html.parser")

quotes = soup.find_all('span', class_='text')

for quote in quotes:
    print(type(quote))
    print(quote.text)
    print()
