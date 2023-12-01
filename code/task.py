class Tomato:
    states = ["отсутствует", "цветение", "зеленый", "красный"]

    def __init__(self, index):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        current_state_index = self.states.index(self._state)
        if current_state_index < len(self.states) - 1:
            self._state = self.states[current_state_index + 1]

    def is_ripe(self):
        return self._state == "красный"


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i + 1) for i in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []

    def plant_info(self):
        for tomato in self.tomatoes:
            print(f"Томат {tomato._index}: {tomato._state}")


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.tomatoes:
            if self._plant.all_are_ripe():
                harvested_tomatoes = [tomato._index for tomato in self._plant.tomatoes]
                self._plant.give_away_all()
                return harvested_tomatoes
            else:
                print("Внимание: не все помидоры созрели. Соберите урожай, когда все томаты будут спелыми.")
        else:
            print("Внимание: нет томатов для сбора урожая.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")


# Тесты
# Тест 1:
Gardener.knowledge_base()

# Тест 2:
tomato_bush = TomatoBush(5)
gardener = Gardener("Иван", tomato_bush)

# Тест 3:
gardener.work()
gardener.work()
tomato_bush.plant_info()

# Тест 4:
harvested_tomatoes_attempt_1 = gardener.harvest()
print(f"{gardener.name} собрал урожай (попытка 1): {harvested_tomatoes_attempt_1}")

gardener.work()
gardener.work()
tomato_bush.plant_info()

# Тест 5:
harvested_tomatoes_final = gardener.harvest()
print(f"{gardener.name} собрал урожай (окончательно): {harvested_tomatoes_final}")