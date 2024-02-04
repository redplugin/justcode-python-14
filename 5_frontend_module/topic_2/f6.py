# from functools import reduce

# a = [1, 4, 5]

# res = reduce(lambda x, y: x + y, a)

# print(res)

def outer(x):
    def inner(y):
        return x + y
    
    return inner

addFive = outer(5)
print(addFive(3))
