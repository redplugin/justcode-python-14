class People:
    def __init__(self, name, surname, gender=None):
        self.name = name
        self.surname = surname
        self.gender = gender

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        if self.gender != other.gender:
            res = People("Max", f"{self.surname}-{other.surname}")
        else:
            res = "Не правильно же!"
        return res






























# class People:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def __repr__(self):
#         return f"{self.name} ({self.age}, {self.height})"
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __lt__(self, other):
#         return self.age < other.age


