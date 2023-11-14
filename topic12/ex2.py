
def get_sum(a, b):
    if type(b) == str:
        raise ValueError("b почему то строка!")
    return a + b


try:
    a = get_sum(12, "30")
except ValueError as e:
    a = -1
    print(f"Ошибка... {e}")

print(a)
print("Другие важные дела не зависимые от new_a")
