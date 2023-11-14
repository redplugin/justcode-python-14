# Создание класса - инициализация
# Создание объекта - создание экземпляра класса - instance - инстанс
# метод - функция внутри класса
# поля, своиства, параметры, аттрибуты - переменные внутри класса

# get, set  -- взять, установка

# Родительский класс, parent класс/ супер класс - выше уровнем класс
# Подкласс, child класс, класс ребонок - ниже уровнем класс, имеет все свойства parent класса

class Building:
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors

    def greeting(self):
        print(f"Привет, я здание {self.name}!")

    def __str__(self):
        return f"Здание {self.name}, по адресу {self.address}, с высотой {self.floors} этажей."


class BusinessCenter(Building):
    def __init__(self, name, address, floors, staff):
        super().__init__(name, address, floors)

        self.staff = staff

    def __str__(self):
        return f"{super().__str__()} Здесь работает {self.staff} людей."



# muit = Building(name="MUIT", address="Manasa 94", floors=10)
alatau = BusinessCenter(name="Alatau", address="Abaya Roz", floors=17, staff=40)

alatau.greeting()
print(alatau)


# print(muit.greeting())



