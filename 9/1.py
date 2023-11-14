# Дано радиус r, нужно найти площадь окружности по формуле
# S = π × r^2 .

# • Дано радиус r, нужно найти объем сферы по формуле
# V = 4/3 × π × r 3 .
# • Надо найти радиан от градуса угла.)
from math import pi, pow


def get_area(r):
    s = pi * pow(r, 2)
    return s


r = 12
area = get_area(r)

print(f"area: {area}")




