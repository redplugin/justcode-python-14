class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.available = False

    def get_available(self):
        return self.available

    def set_available(self, new_available):
        self.available = new_available

    def __repr__(self):
        return f'"{self.title}" by {self.author}'






