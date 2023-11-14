# Написать функцию, которая будет принимать список чисел,
# и возвращать
# сумму четных. Попробовать с несколькими списками.


def sum_of_evens(l):
    res = 0
    for number in l:
        if number % 2 == 0:
            res = res + number

    return res

l = [2, 5, 10, 4]
result = sum_of_evens(l)
print(result)

