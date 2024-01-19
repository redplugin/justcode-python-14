


s = "hello world from justcode!"
# { "h": 1, "e": 2, "l": 3 }
res = {}

for i in s:
    if res.get(i) == None:
        res[i] = 1
    else:
        res[i] = res[i] + 1

print(res)

