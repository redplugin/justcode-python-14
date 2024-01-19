
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

page_size = 3

# print(data[0:3])  # page=1

# page = 1
# print(data[(page-1) * page_size: ((page-1) * page_size) + page_size])

for page in range(1, 4):
    print(f"page {page}")
    print(data[(page - 1) * page_size: ((page - 1) * page_size) + page_size])
    print()
# [0: 3] page=1
# [3: 6] page=2
# [6: 9] page=3

# print(data[3:6])  # page=2
# print(data[6:9])  # page=3




