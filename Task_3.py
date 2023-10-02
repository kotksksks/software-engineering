class Book:
    default_year = 2023

    def __init__(self, author_name, book_title, read_month):
        self.author = author_name
        self.title = book_title
        self.month = read_month

    def get_full_info(self):
        self.month = self.month[:-1] + 'e' if self.month not in ['март', 'апрель'] else self.month + 'e'
        return f'{self.author} "{self.title}", прочитана в {self.month} {self.default_year} г.'

    def get_surname(self):
        return self.author.split()[-1]


purchased_book = Book('Криста Вольф', 'Один день года (1960-2000)', 'сентябрь')
print(purchased_book.get_full_info())


class NonfictionBook(Book):
    def __init__(self, author_name, book_title, read_month, book_theme):
        super().__init__(author_name, book_title, read_month)
        self.theme = book_theme

    def get_most_frequent_theme(purchased_books):
        themes = [book.theme for book in purchased_books]
        most_frequent_theme = max(set(themes), key=themes.count)
        return most_frequent_theme


purchased_books = [NonfictionBook('Морис Дрюон', 'Париж от Цезаря до Людовика Святого', 'январь', 'история'),
                   NonfictionBook('Кирилл Бабаев', 'История человечества в великих документах', 'июль', 'история'),
                   NonfictionBook('Дарелл Хафф', 'Как лгать при помощи статистики', 'июнь', 'политика')]
for book in purchased_books:
    print(book.get_full_info())
print('Самая популярная тематика прочитанных книг: ' + NonfictionBook.get_most_frequent_theme(purchased_books))
