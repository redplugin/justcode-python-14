
data = [
    {'name': '1'},  # 0
    {'name': '2'},
    {'name': '3'},
    {'name': '4'},
    {'name': '5'},
    {'name': '6'},
    {'name': '7'},
    {'name': '8'},
    {'name': '9'}   # 8
]

page_size = 5

for page in range(1, 6):
    print(f"page {page}")

    offset = (page - 1) * page_size
    limit = offset + page_size

    print(data[offset: limit])
    print()





