def sum_two_numbers():
    try:
        num = float(input('Введите число:\n'))
        res = num + 2
        return res
    except ValueError:
        return 'Неподходящий тип данных. Ожидалось число.'

print(sum_two_numbers())
print(sum_two_numbers())
