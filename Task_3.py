from datetime import datetime
from time import sleep


def show_time():
    for _ in range(5):
        current_time = datetime.now().replace(microsecond=0)
        print(current_time)
        sleep(1)


if __name__ == '__main__':
    show_time()
