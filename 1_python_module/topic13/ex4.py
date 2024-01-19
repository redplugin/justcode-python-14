# классы называются в ед числе

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Звук животного")
        # pass
        # return None

    def __repr__(self):
        return f"{self.name}, возраст: {self.age}"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    # def make_sound(self):
    #     super().make_sound()
        # print(f"Чик-Чирик")

    def __repr__(self):
        return f"{super().__repr__()}, размах крыльев {self.wing_span}"


class Eagle(Bird):
    def __init__(self, name, age, wing_span, years_in_care):
        super().__init__(name, age, wing_span)
        self.years_in_care = years_in_care


# a = Bird('Беркут', 12, 240)
a = Eagle('Кеша', 12, 240, 10)
print(a)
a.make_sound()








