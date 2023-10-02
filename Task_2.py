def read_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8-sig')
        content = file.read()
        if not content:
            raise Exception("Файл пустой")
        print(content)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    read_file('empty.txt')
    read_file('nonempty.txt')