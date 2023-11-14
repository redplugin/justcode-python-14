class Building:
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors

    def greeting(self):
        print(f"Zdanie2 {self.name}")

    def get_name(self):
        return self.name

    def set_name(self, new_name ):
        self.name = new_name

    def __str__(self):
        return f"Здание {self.name}, адрес {self.address}, этажей { self.floors} "


muit = Building(name="MUIT", address="Manasa 94", floors=10)
kbtu = Building(name="KBTU", address="Tole bi 56", floors=15)

print(muit.get_name())
muit.set_name("AUES")
print("after")
print(muit.get_name())
