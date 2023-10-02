nums = list(map(int, input('Введите числа через пробел: ').split()))


def count_average(*args):
    args_amount = len(list(args))
    average = sum(args) / args_amount
    if int(average) == average:
        average = int(average)
    return average


if __name__ == '__main__':
    print(f'Среднее арифметическое равно:', count_average(*nums))
