import json

file1 = open("example.json", 'r')

# data = file1.read()
data = json.load(file1)

print(type(data))
print(data)

print(data["name"])


# file2 = open("example.json", 'w')
# d = {"name": "JustCode1", "age": 25}
# json.dump(d, file2)


