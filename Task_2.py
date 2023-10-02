import random


def dice():
    edge = random.randint(1, 6)
    if edge == 5 or edge == 6:
        return 'Вы победили'
    elif edge == 1 or edge == 2:
        return 'Вы проиграли'
    else:
        print('Повтор броска')
        return dice()


if __name__ == '__main__':
    print(dice())
