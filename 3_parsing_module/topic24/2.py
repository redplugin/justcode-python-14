
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, "html.parser")

quotes = soup.find_all('span', class_="text")
authors = soup.find_all('small', class_="author")
tags = soup.find_all('div', class_="tags")

for i in range(len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    tag_details = tags[i].find_all('a')
    tags_list = [tag.text for tag in tag_details]
    print(", ".join(tags_list))
    print()
