class GreaterThanTenError(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_sum(a, b):
    if b > 10 or a > 10:
        raise GreaterThanTenError('Наша функция работает только с числами меньше десяти!')
    return a + b


a = 9
b = 30

try:
    result = get_sum(a, b)
    print(result)
except TypeError as e:
    print(f"Здесь ошибка: {e}")
except GreaterThanTenError as e:
    print(f"Здесь ошибка 2: {e}")

print("Finished!")


