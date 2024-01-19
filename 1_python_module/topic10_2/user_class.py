class User:
    def __init__(self, name):
        self.name = name
        self.books = []

    def take_book(self, book):
        if book.get_available() is True:
            self.books.append(book)
            book.set_available(False)
            print("Книгу взяли на чтение!")
        else:
            print("Книга не доступна!")

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.set_available(True)
        else:
            print("У вас нет этой книги!")

    def get_books(self):
        return self.books