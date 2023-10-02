import csv


def record_expenses(expenses):
    date = input('Введите дату: ')
    category = input('Введите категорию: ')
    amount = float(input('Введите сумму: '))
    expenses.append({'date': date, 'category': category, 'amount': amount})
    file = open('expenses.csv', 'a')
    writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount'])
    writer.writerow(expenses[-1])


def view_expenses(expenses):
    file = open('expenses.csv', 'r')
    reader = csv.DictReader(file, fieldnames=['date', 'category', 'amount'])
    for row in reader:
        print(f"{row.get('date', ''), row.get('category', ''), row.get('amount', '')}")


expenses = []

while True:
    print('1. Добавить запись')
    print('2. Просмотреть записи')
    choice = int(input('Введите номер действия: '))

    if choice == 1:
        record_expenses(expenses)
    elif choice == 2:
        view_expenses(expenses)
        break
