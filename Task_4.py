lists = [[2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4], [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4], [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]]

def correct_grades(lst):
    new_lst = [4 if i == 3 else i for i in lst if i != 2]
    print(f'Новый список оценок:', *new_lst)

for lst in lists:
    correct_grades(lst)
