def func_call(f, l):
    result = []
    for number in l:
        square = f(number)
        result.append(square)

    return result


def func(a):
    return a


numbers = [9, 5, 3, 6, 2]
r = func_call("12", numbers)

print(r)
