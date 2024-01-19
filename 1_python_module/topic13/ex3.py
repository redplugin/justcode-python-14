
res = None
try:
    with open('example.txt', 'r') as file:
        res = file.read()
    # file = open('example.txt', 'r')
    # res = file.read()
except FileNotFoundError as e:
    print(f"Ошибка: {e}")
    file = open('example.txt', 'w')
    print("Исправлено!")
except Exception as e:
    print(f"Нежданчик ошибка: {e}")
    file = open('example.txt', 'w')
    print("Исправлено!")
else:
    print("Ошибок не было!")
finally:
    file.close()
    print("Ha-Ha-Ha")


print(res)








