import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, "html.parser")

borders = soup.find_all("div", class_='w-full rounded border')

elements = []
for border in borders:
    elements.append(border.find("div", class_='p-4'))

for elem in elements:
    print(elem)
    print()
    title_elem = elem.find('a')
    print(title_elem.text)

    # ...

    print()

