# Написать функцию, которая будет принимать произвольное
# число аргументов, и будет возвращать среднее арифметическое
# значение.

def mean_value(*args):
    res = 0
    if len(args) == 0:
        print("test1")
        return res
    print("test3")
    for number in args:
        res = res + number

    mean_v = res / len(args)
    print("test2")
    return mean_v

result = mean_value(12, 56)
print(result)





