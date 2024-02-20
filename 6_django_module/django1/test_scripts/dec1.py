#
# def to_upper(func):
#
#     def wrapper():
#         print("Перед")
#         a = func()
#         print("После")
#         return a.upper()
#
#     return wrapper
#
#
# @to_upper
# def say_hi():
#     print("Внутри функции...")
#     return "Hello World"


def to_square(func):
    def wrapper(a, b):
        print("Перед", a, b)
        # print("Проверка юзера... Есть ли доступ, авторизован ли...")

        res = func(a*a, b*b)

        print("После")
        return res ** 2

    return wrapper


@to_square
def get_sum(a, b):
    print("Внутри функции...", a, b)
    return a + b


print(get_sum(2, 3))


