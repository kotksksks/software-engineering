# Проверить, что строка начинается и заканчивается одним и тем же знаком, цифрой или буквой
string = str(input('Введите строку: '))
res = string[0].lower() == string[-1].lower()
print('Результат:', res)
