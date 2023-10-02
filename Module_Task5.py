from math import sqrt


def count_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    return f'Площадь равна {round(area, 4)}'
