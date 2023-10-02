# Декоратор функций, который логирует результаты вызова функции
def my_decorator(func):
    def wrapper(name):
        func(name)  # Вызываем функцию с аргументом name

    # Возвращаем обёртку, которая будет вызываться вместо оригинальной функции
    return wrapper


# Декоратор @my_decorator добавляет логирование к функции say_bye
@my_decorator
def say_hello(name):
    print('Добрый день,', name)


# Декоратор @my_decorator добавляет логирование к функции say_bye
@my_decorator
def say_bye(name):
    print('Доброй ночи,', name)


# Основная часть программы, которая вызывает функции
name = input('Введите своё имя: ')  # Запрашиваем имя пользователя
say_hello(name)  # Вызываем функцию say_hello с аргументом name
say_bye(name)  # Вызываем функцию say_bye с аргументом name
