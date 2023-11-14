class Building :

    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors

    def turn_on(self):
        print("svet vkl")

    def greeting(self):
        print(f"Zdanie2 {self.name}")

    def __str__(self):
        return f"Здание {self.name}, адрес {self.address}, этажей { self.floors} "


muit = Building(name="MUIT", address="Manasa 94", floors=10)
kbtu = Building(name="KBTU", address="Tole bi 56", floors=15)

print(muit)
print("after changes:", muit)


muit.greeting()
# kbtu.greeting()