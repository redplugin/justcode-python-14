def sum_of_n(a, c, *args, **kwargs):   # args = arguments; kwargs = keyword arguments
    print(f"kwargs: {kwargs}")
    print(f"args: {args}")
    print(f"a: {a}")
    print(f"c: {c}")


res = sum_of_n(5, 11, 12, 77, y=9, b = 90)
print(res)
