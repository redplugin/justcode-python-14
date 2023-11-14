# Отсортировать список словарей по длине значении ключа "name";

people = [
    {
        "name": "Ulan Kospan",
        "age": 23
    }, {
        "name": "Alex",
        "age": 18
    }, {
        "name": "Aizat",
        "age": 25
    }
]


sorted_people = sorted(people, key=lambda x: len(x['name']), reverse=True)

print(sorted_people)



