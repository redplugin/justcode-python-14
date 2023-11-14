
numbers = [9, 5, 3, 6, 2]
# numbers = [9, 5, 3, 6, 2]

func = lambda x: x ** 2

squared_numbers = []
for number in numbers:
    y = func(number)
    squared_numbers.append(y)



# squared_numbers = list(map(lambda x: x ** 2, numbers))

print(f"usual func: {squared_numbers}")








# def func(x):
#     return x ** 2
#
#


