class Tomato:
    states = ['отсутствует', 'цветение', 'зелёный', 'красный'] # Список стадий зрелости томата

    # Установка начального состояния роста
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    # Переводит томат в следующее состояние роста
    def grow(self):
        self._state = Tomato.states[(Tomato.states.index(self._state) + 1) % len(Tomato.states)]

    # Проверка спелости
    def is_ripe(self):
        return self._state == 'красный'

class TomatoBush:
    # Список всех томатов
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    # Выращивание на кусте
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверка спелости
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Сбор всех на кусте
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    # Инициализация с именем и растением
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Выращивание на кусте
    def work(self):
        self._plant.grow_all()

    # Проверка спелости
    def harvest(self):
        # Если спелые, то сбор всех на кусте
        if self._plant.all_are_ripe():
            print(f'{self.name} собрала урожай')
            self._plant.give_away_all()
        else:
            print('Томаты ещё не красные')

    # Статический метод, выводит "справку"
    @staticmethod
    def knowledge_base():
        print('Справка по садоводству')

# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов классов TomatoBush и Gardener
bush = TomatoBush(5)
gardener = Gardener('Мария', bush)

# Уход за кустом с помидорами
for _ in range(10):
    gardener.work()

# Проба сбора когда не все созрели
gardener.harvest()

# Продолжение ухода
for _ in range(5):
    gardener.work()

# Сбор урожая
gardener.harvest()
