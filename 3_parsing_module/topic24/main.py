
import requests

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

data = response.text

print(data)
print('\n\n\n')
rows = data.split('\n')

for row in rows:
    if 'span class="text"' in row:
        v1 = row.strip()
        l = v1.index('>')
        v2 = v1[l+1:]

        r = v2.index('<')

        res = v2[:r]
        print(res)
        # print("============")
