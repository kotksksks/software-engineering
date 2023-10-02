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
print(purchased_book.get_surname())
