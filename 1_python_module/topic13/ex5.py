
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, возраст: {self.age}"


class Bird(Animal):
    cnt = 0

    def __init__(self, name, age, wing_span):

        super().__init__(name, age)
        self.wing_span = wing_span

        Bird.cnt += 1

    def __str__(self):
        return f"{super().__repr__()}, размах крыльев {self.wing_span}"

    def __repr__(self):
        return f"{super().__repr__()}, размах крыльев {self.wing_span}"


a = Bird('Беркут', 12, 240)
print(a)

b = Bird('Колибри', 1, 2)
print(b)

c = Bird('Попугай', 20, 100)
print(c)

x = Bird('Птица', 20, 100)
print(x)

print(f"Кол-во птиц: {Bird.cnt}")




















