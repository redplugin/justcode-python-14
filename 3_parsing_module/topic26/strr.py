

s = "\n\n\nHello World\n      ?  18:19\n*\n#neonas\n\n"

# print(s.replace(" ", ""))
splitted = s.strip().split("\n")
print(splitted)

for line in splitted:
    print(line.replace('?', '').strip())



