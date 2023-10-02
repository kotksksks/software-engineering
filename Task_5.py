lists = [[1, 1, 3, 3, 1], [5, 5, 5, 5, 5, 5, 5], [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]]


def convert_to_set(lst, sts):
    for i in range(len(lst)):
        if lst[:i + 1].count(lst[i]) != 1:
            sts.add(str(lst[i]) * lst[:i + 1].count(lst[i]))
    return sts


for lst in lists:
    sts = set(lst)
    print(convert_to_set(lst, sts))
