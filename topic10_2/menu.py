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
library.add_book(book3)


print(f"Меню библиотеки:\n"
      f"1. Список всех книг\n"
      f"2. Взять книгу\n\n")

user_input = input("Выберите действие[1-2]: ")

if user_input == '1':
    print(library.get_books())
elif user_input == '2':
    books = library.get_books()
    for i in range(len(books)):
        print(f"{i}. {books[i]}")

    book_number = int(input("Выберите книгу: "))
    user1.take_book(books[book_number])



















