class Book:
    __default_year = 2023

    def __init__(self, author_name, book_title, read_month):
        self.__author = author_name
        self.__title = book_title
        self.__month = read_month

    def get_full_info(self):
        self.__month = self.__month[:-1] + 'e' if self.__month not in ['март', 'апрель'] else self.__month + 'e'
        return f'{self.__author} "{self.__title}", прочитана в {self.__month} {self.__default_year} г.'

    def __str__(self):
        return f'{self.__author}, {self.__title}'

    def __get_surname(self):
        return self.__author.split()[-1]

    def get_author(self):
        return self.__author


purchased_book = Book('Криста Вольф', 'Один день года (1960-2000)', 'сентябрь')
print(purchased_book.get_full_info())


class NonfictionBook(Book):
    def __init__(self, author_name, book_title, read_month, book_theme):
        super().__init__(author_name, book_title, read_month)
        self.__theme = book_theme

    def get_most_frequent_theme(purchased_books):
        themes = [book._NonfictionBook__theme for book in purchased_books]
        most_frequent_theme = max(set(themes), key=themes.count)
        return most_frequent_theme


purchased_books = [
    NonfictionBook('Морис Дрюон', 'Париж от Цезаря до Людовика Святого', 'январь', 'история'),
    NonfictionBook('Кирилл Бабаев', 'История человечества в великих документах', 'июль', 'история'),
    NonfictionBook('Дарелл Хафф', 'Как лгать при помощи статистики', 'июнь', 'политика')]

for book in purchased_books:
    print(book.get_full_info())
print('Самая популярная тематика прочитанных книг: ' + NonfictionBook.get_most_frequent_theme(purchased_books))
