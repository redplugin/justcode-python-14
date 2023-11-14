
vowels = ["a", "e", "i", "o", "u"]

s = "hello world from justcode"
res = set()
# res = []
for i in s:
    if i in vowels:
        res.add(i)
        # res.append(i)

print(res)

