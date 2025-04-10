from pygame import *

# Классы

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга '{title}' была успешно удалена.")
                return
        print(f"Книги с названием '{title}' не найдено.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                print(book.display_info())
                return
        print(f"Книги с названием '{title}' не найдено.")

    def show_books(self):
        if not self.books:
            print("В библиотеке нет доступных книг.")
        else:
            for book in self.books:
                print(book.display_info())

def main():
    library = Library()

# Цикл и работа программы
    
    while True:
        print("\nМеню:")
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книгу по названию")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == "1":
            library.show_books()
        elif choice == "2":
            title = input("Введите название книги: ")
            author = input("Введите имя автора: ")
            year = int(input("Введите год издания: "))
            new_book = Book(title, author, year)
            library.add_book(new_book)
        elif choice == "3":
            title = input("Введите название книги для удаления: ")
            library.remove_book(title)
        elif choice == "4":
            title = input("Введите название книги для поиска: ")
            library.find_book(title)
        elif choice == "5":
            print("Завершение работы")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
