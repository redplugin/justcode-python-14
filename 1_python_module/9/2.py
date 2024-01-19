# • Написать игру, где два пользователя кидают кости, и вывести имя выигравшего юзера.
# Кости - кубик с 1-6 точками на каждой стороне.
from random import randint

a = randint(1, 6)
print(f"Ulan: {a}")

b = randint(1, 6)
print(f"Nurdaulet: {b}")

if a > b:
    print("Ulan pobeditel'!")
elif b > a:
    print("Ulanu prosto ne povezlo!")
else:
    print("Ni4ya!")




