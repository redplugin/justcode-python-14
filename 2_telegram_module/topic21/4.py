

data = [
    {"name": "1"},
    {"name": "2"},
    {"name": "3"},
    {"name": "4"},
    {"name": "5"}
]

PAGE = 0
PAGE_SIZE = 3

def print_data(data, offset, limit):
    res = data[offset: limit]
    print(res)

for i in range(4):
    print_data(
        data=data,
        offset=PAGE * PAGE_SIZE,
        limit=PAGE * PAGE_SIZE + PAGE_SIZE
    )
    PAGE += 1

    print("\n\n")







