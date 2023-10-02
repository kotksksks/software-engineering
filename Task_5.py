# Программа должна создать файл с именем random.txt и записать в него случайные числа от 1 до 10 в количестве 25 штук

from random import randint

file = open('random.txt', 'w')
file.writelines([str(randint(1, 10)) + '\n' for _ in range(25)])
file.close()
