

a = "123a"

try:
    new_a = int(a)
    check = 12 / 0
except ValueError as e:
    a = a[:-1]
    new_a = int(a)
    print(f"с new_a ожидаемая ошибка, исправили!")
except Exception as e:
    print(f"Неожиданная ошибка! {e}")
else:
    print("Не было ошибки!")
finally:
    print("Ha-Ha-Ha")

# print(new_a)

print("Другие важные дела не зависимые от new_a")
