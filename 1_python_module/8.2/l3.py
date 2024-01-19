
numbers = [9, 5, 3, 6, 2]
# squared_numbers = list(map(lambda x: x ** 2, numbers))

# words = ["hello world", "My name is Ulan", "I am 13"]
joined_words = list(map(lambda x: x.replace(' ', ''), numbers))

print(f"lambda func: {joined_words}")

