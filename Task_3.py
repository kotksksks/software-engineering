from math import sqrt

lists = [[12, 25, 3, 48, 71], [5, 18, 40, 62, 98], [4, 21, 37, 56, 84]]
max_triangle = []
min_triangle = []


def count_area(a, b, c):
    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    area = int(area) if int(area) == area else round(area, 4)
    return area


for lst in lists:
    max_triangle.append(max(lst))
    min_triangle.append(min(lst))

print(f'Площадь наибольшего равна {count_area(*max_triangle)}, площадь наименьшего равна {count_area(*min_triangle)}')
