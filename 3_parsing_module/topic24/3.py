
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, "html.parser")

full_quotes = soup.find_all('div', class_="quote")

for full_quote in full_quotes:
    quote = full_quote.find('span', class_='text')
    author = full_quote.find('small', class_='author')
    tags = full_quote.find_all('a', class_='tag')

    print("Quote: ", quote.text)
    print("Author: ", author.text)
    for tag in tags:
        print(tag.text, end=", ")
    print("\n\n")

