tuples = ['(1, 2, 3), 1)', '(1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)', '(2, 4, 6, 6, 4, 2), 9)']


def remove_element(tple, element):
    lst = list(tple)
    if element in lst:
        lst.remove(element)
        return tuple(lst)
    else:
        return tple


for tpl in tuples:
    tple = tuple(map(int, tpl[:-4].strip('()').split(',')))
    element = int(tpl[-2:-1][0])
    new_tuple = remove_element(tple, element)
    print(new_tuple)
