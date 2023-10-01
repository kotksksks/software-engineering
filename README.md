# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

![Меню](https://github.com/segamega-drive/software_engineering/blob/fe71cac654899315164ba881b67ffd8241505f38/img/7.1.1.png)

```python
import re

file = open('article.txt', 'r', encoding='utf-8-sig')
words = file.read().split()
stopwords = ['в', 'на', 'и', 'с', 'к', 'а']
print(f'Длина статьи: {len(words)} слов.')


def clean_text(words, stopwords):
    words = [re.sub(r'[,()."—:«»]', '', i) for i in words if i not in stopwords and len(i) > 1]
    return words


def find_most_frequent(words):
    words = clean_text(words, stopwords)
    num_freq = {}
    for word in words:
        num_freq[word] = num_freq.get(word, 0) + 1
    sorted_num_freq = sorted(num_freq.items(), key=lambda item: item[1])
    top = sorted_num_freq[-1]
    return top


res = find_most_frequent(words)
print(f'Самое встречающееся слово: "{res[0]}". Встречается {res[1]} раз.')

file.close()
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/fe71cac654899315164ba881b67ffd8241505f38/img/7.1.png)

## Выводы
В данном задании мы знакомимся с 
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/e15899fc1fb28ef3e44cdcb1b711ff85349d9e5a/img/5.2.png)

## Выводы
В данном задании 
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```python
import re

file = open('input.txt', 'r', encoding='utf-8-sig')

number_of_words = 0
number_of_lines = 0
number_of_characters = 0

for string in file:
    number_of_words += len(string.split())
    number_of_lines += 1
    for letter in string:
        number_of_characters += 1 if re.match(r'[a-zA-Z]+', letter) else 0

print('Input file contains:', f'{number_of_characters} letters', f'{number_of_words} words', f'{number_of_lines} lines',
      sep='\n')

file.close()
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/fe71cac654899315164ba881b67ffd8241505f38/img/7.3.png)

## Выводы
В данном задании 

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

```python
import re

file = open('input1.txt', 'r', encoding='utf-8-sig')
stopwords = file.read().split()
string = '''Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!'''


def censor_text(string, stopwords):
    for stopword in stopwords:
        string = re.sub(re.escape(stopword), lambda x: '*' * len(x.group()), string, flags=re.IGNORECASE)
    return string


res = censor_text(string, stopwords)
print('Заменённый текст:\n' + res)

file.close()
```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/fe71cac654899315164ba881b67ffd8241505f38/img/7.4.png)

## Выводы
В данном задании 

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```python

```

### Результат
![Меню](https://github.com/segamega-drive/software_engineering/blob/e15899fc1fb28ef3e44cdcb1b711ff85349d9e5a/img/5.5.png)

## Выводы
В данном задании 

## Общие выводы по теме
В данной теме мы 
