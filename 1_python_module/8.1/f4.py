def sum_of_n(a, *args):
    print(f"a: {a}")  # args = arguments
    print(f"args: {args}")  # args = arguments
    res = 0
    res = res + a
    for number in args:
        res = res + number

    return res

res = sum_of_n(99, 5, 10, 4, 9)
print(res)


