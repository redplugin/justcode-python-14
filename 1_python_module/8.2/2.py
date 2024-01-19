# Отсортировать список словарей по длине значении ключа "name";

people = [
    {
        "name": "Ulan Kospan",
        "age": 45
    }, {
        "name": "Alex",
        "age": 18
    }, {
        "name": "Aizat",
        "age": 25
    }
]

under_30 = list(filter(lambda x: x['age'] >= 30, people))
beyond_30 = list(filter(lambda x: x['age'] < 30, people))

print(under_30)
print(beyond_30)



