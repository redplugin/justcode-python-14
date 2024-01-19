
add = lambda x, y: x + y

a = int(input('a = '))
b = int(input('b = '))
op = input('operator = ')

result = None

if op == '+':
    result = add(a, b)


print(f"result: {result}")


