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
![Меню](https://github.com/segamega-drive/software_engineering/blob/e15899fc1fb28ef3e44cdcb1b711ff85349d9e5a/img/5.1.png)

## Выводы
В данном задании мы знакомимся с 
  
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
![Меню](https://github.com/segamega-drive/software_engineering/blob/e15899fc1fb28ef3e44cdcb1b711ff85349d9e5a/img/5.2.png)

## Выводы
В данном задании 
  
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

purchased_books = [NonfictionBook('Морис Дрюон', 'Париж от Цезаря до Людовика Святого', 'январь', 'история'), NonfictionBook('Кирилл Бабаев', 'История человечества в великих документах', 'июль', 'история'), NonfictionBook('Дарелл Хафф', 'Как лгать при помощи статистики', 'июнь', 'политика')]
for book in purchased_books:
    print(book.get_full_info())
print(NonfictionBook.get_most_frequent_theme(purchased_books))
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/e15899fc1fb28ef3e44cdcb1b711ff85349d9e5a/img/5.3.png)

## Выводы
В данном задании 

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/e15899fc1fb28ef3e44cdcb1b711ff85349d9e5a/img/5.4.png)

## Выводы
В данном задании 

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/e15899fc1fb28ef3e44cdcb1b711ff85349d9e5a/img/5.5.png)

## Выводы
В данном задании 

## Общие выводы по теме
В данной теме мы 
