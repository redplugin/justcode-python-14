
class Shkaf:
    def __init__(self):
        self.door = "Closed"

    def get_candies(self):
        if self.door == "Open":
            print("Взяли все конфеты!")
        else:
            print("Дверь закрыта:(")

    def open_door(self):
        self.door = "Open"
        print("Открыли дверь!")

    def close_door(self):
        self.door = "Closed"
        print("Закрыли дверь!")

    def __enter__(self):
        # print("Мы зашли в контекст менеджер!")
        self.open_door()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_door()
        # print("Мы вышли из контекст менеджер!")


with Shkaf() as s:
    s.get_candies()
    print("Check1")

print("Check2")
