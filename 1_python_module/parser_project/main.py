import requests
from bs4 import BeautifulSoup

url_basic = 'https://tengrinews.kz/'
news_text = ''

response = requests.get(url_basic)
soup = BeautifulSoup(response.text, "html.parser")

first = soup.select('div[class="tn-main-news-grid"]')
url_list = first[0].find_all('a')
for i in url_list:
    print('+++++++++++++++++++++')
    url = i.get('href')
    if url[0:5] == 'https':
        response = requests.get(url)
    else:
        response = requests.get(url_basic + url)

    soup = BeautifulSoup(response.text, "html.parser")
    news = soup.select('div[class="tn-news-content"]')

    news_text = ''
    auth = ''

    if len(news) != 0:
        text_list = news[0].find_all(name='p')
        author = soup.select('li[class="author"]')
        title = soup.select('h1[class="tn-content-title"]')
        tit = title[0].text

        print(tit)
        for x in text_list:
            news_text += x.text + '\n'

        if len(author) != 0:
            auth = author[0].text

        print(news_text)
        print(auth)

        with open('news.txt', 'w', encoding='utf-8') as file:
            file.write(tit + '\n' + news_text + '\n' + auth)