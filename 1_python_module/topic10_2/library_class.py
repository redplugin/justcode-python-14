class Library:
    def __init__(self):
        self.book_storage = []

    def add_book(self, new_book):
        self.book_storage.append(new_book)
        new_book.set_available(True)

    def remove_book(self, book):
        self.book_storage.remove(book)
        book.set_available(False)

    def get_books(self):
        return self.book_storage
