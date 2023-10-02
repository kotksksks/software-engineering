# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
- Сбитнева Мария Алексеевна
- ЗПИЭ-20-2

| Задание | Сам_раб |
| ------  | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Book:
    isbn = '978-5-7584-0386-0'


purchased_book = Book()
print(purchased_book.isbn)
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/817175a0fd49a2b6ef0f97a727de1364b2e0a8f3/img/8.1.png)

## Выводы
Класс — структура данных, определяющая тип объекта и его свойства. Объект — экземпляр класса. 

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/817175a0fd49a2b6ef0f97a727de1364b2e0a8f3/img/8.2.png)

## Выводы
В данном задании мы дополняем класс атрибутами и методами. В данном случае создан класс Book с атрибутами author, title и month. Созданы методы get_full_info() и get_surname() для получения полной информации о книге и фамилии автора.
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/817175a0fd49a2b6ef0f97a727de1364b2e0a8f3/img/8.3.png)

## Выводы
В данном задании создан класс NonfictionBook, который наследует (получает все атрибуты и методы) Book. Метод super() используется для вызова метода родительского класса. Создан статический метод get_most_frequent_theme(), который вычисляет наиболее часто встречаемую тематику книг.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
    print(book.get_author())
print('Самая популярная тематика прочитанных книг: ' + NonfictionBook.get_most_frequent_theme(purchased_books))

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/817175a0fd49a2b6ef0f97a727de1364b2e0a8f3/img/8.4.png)

## Выводы
В данном задании рассматривается инкапсуляция, позволяющая ограничить доступ к выбранным методам и переменным внутри класса. Подчёркивание перед именами методов и атрибутов делает их приватными. Одиночное подчеркивание используется для обозначения доступа только внутри класса и его подклассах, двойное подчеркивание используется для обозначения доступа только внутри класса.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/817175a0fd49a2b6ef0f97a727de1364b2e0a8f3/img/8.5.png)

## Выводы
В данном задании рассматривается полиморфизм,то есть способность одной функции/метода работать с различными типами. За счёт одинакового имени метода в разных классах и использования метода дочернего класса при вызове метода родительского класса он был использован в методе get_full_info. Он определен в классах Book и Nonfiction Book. Когда мы вызываем метод get_full_info для объекта класса NonfictionBook, выполняется метод get_full_info класса NonfictionBook, а не метод get_full_info класса Book.

## Общие выводы по теме
В данной теме мы рассмотрели основы ООП. Ознакомились с понятиями клааса, объекта, наследования, инкапсуляции, полиморфизма, а также методов. Класс — как шаблон для создания объектов, объект — экземпляр класса. Наследование позволяет создавать новые классы на основе уже существующих. Инкапсуляция позволяет скрыть детали реализации класса. Полиморфизм позволяет использовать объекты разных классов в качестве объектов одного и того же типа.
