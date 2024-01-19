from book_class import Book
from library_class import Library
from user_class import User

user1 = User(name="Alex")

library = Library()

book1 = Book(title="Harry Potter", author="J.K. Rowling")
book2 = Book(title="1984", author="Oruell")
book3 = Book(title="Книга3", author="Автор")


library.add_book(book1)
library.add_book(book2)

books = library.get_books()
print("Книги библиотеки: ", books)

print(f"Юзер {user1.name} берет книгу {book1}")
user1.take_book(book1)

print("Книги у юзера: ", user1.get_books())

print(f"Юзер {user1.name} возвращает книгу {book1}")
user1.return_book(book1)
print("Книги у юзера: ", user1.get_books())


# print(book1.get_available())
# book1.set_available(True)
# print("После изменения: ", book1.get_available())

# print(str(book1).replace(" ", "*"))












