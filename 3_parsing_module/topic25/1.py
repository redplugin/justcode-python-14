import requests
from bs4 import BeautifulSoup

base_url = 'https://stopgame.ru'
main_url = base_url + '/topgames'

response = requests.get(main_url)

data = response.text

soup = BeautifulSoup(data, "html.parser")
# print(f"soup type: {type(soup)}")
top_five = soup.find_all('a', class_='_card_1ovwy_1')
# print(f"top five type: {type(top_five)}")


for game_info in top_five[5:10]:
    # print(type(game_info))
    # print(game_info.attrs)

    print(game_info["title"])
    game_detail_url = base_url + game_info["href"]
    print(game_detail_url)

    response = requests.get(game_detail_url)
    detail_data = response.text

    soup = BeautifulSoup(detail_data, "html.parser")

    title = soup.find('h2', class_=lambda value: value and value.startswith('_title'))
    values = soup.find_all('div', class_=lambda value: value and value.startswith('_info-grid__value'))
    print(title.text)

    print(values[0].text)
    print(values[3].text)
    print()

