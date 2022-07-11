from random import randint
from time import sleep
from os import system


class GameOfLife:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self._history = []
        self._current = []
        self._previous = []

    def play(self):
        self.create_random_generation(self.x, self.y)
        try:
            while True:
                self.apply_rules()
                self.print()
        except KeyboardInterrupt:
            # self.save_history()
            exit()

    def save_history(self):
        with open('./history.txt', '+w') as file:
            for generation in self._history:
                file.writelines(
                    list(map(lambda x: str(x)+'\n', generation))
                )
                file.write('\n')

    def create_random_generation(self, x, y):
        self._current = [[randint(0, 1) for _ in range(x)]
                for _ in range(y)]

    def apply_rules(self):
        self._previous = self._current.copy()
        self._history.append(self._previous.copy())
        
        for x in range(self.x):
            for y in range(self.y):
                if self._previous[x][y] == 1:
                    if self.count_alive_neighbours(x, y) < 2:
                        self._current[x][y] = 0

                    if self.count_alive_neighbours(x, y) > 3:
                        self._current[x][y] = 0

                    continue
                if self.count_alive_neighbours(x, y) == 3:
                    self._current[x][y] = 1


    # TODO: fix this (neighbours are not being counted correctly)
    def count_alive_neighbours(self, x, y) -> int:
        total = 0
        neighbours = [
            (x-1, y),
            (x+1, y),
            (x, y+1),
            (x, y-1),
            (x-1, y+1), (x-1, y-1),
            (x+1, y-1),
            (x+1, y+1)
        ]

        for n in neighbours:
            if self.is_alive(n[0], n[1]):
                total += 1

        return total

    def is_alive(self, x, y):
        try:
            if self._previous[x][y] == 1:
                return True
        except IndexError:
            return False
        return False

    def print(self):
        for x in range(self.x):
            for y in range(self.y):
                print(self._current[x][y], end=" ")
            print()
        print()
        sleep(0.1)
        # system('clear')
