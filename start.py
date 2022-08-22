from random import randint
from time import sleep


def main():
    gen = [ 
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ]
    while True:
        pprint(gen)
        gen = apply_rules(gen)
        sleep(0.5)
        


def apply_rules(generation):
    """Will apply the rules of the game to raise a new generation."""
    buffer = generation.copy()

    for x in range(len(generation)):
        for y in range(len(generation[x])):
            if generation[x][y] == 1:
                if count_alive_neighbors(generation, x, y) not in (2, 3):
                    buffer[x][y] = 0
                continue
            if count_alive_neighbors(generation, x, y) == 3:
                buffer[x][y] = 1
    return buffer


def raise_generation(x, y):
    return [ 
        [ randint(0, 1) for _ in range(y) ]
        for _ in range(x)
    ]


def pprint(array):
    for line in array:
        for element in line:
            print(element, end=" ")
        print()


def count_alive_neighbors(array, x, y):
    neighbors = []
    if not is_inside(array, x, y):
        return []
    coordinates = [ 
        (x-1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x, y-1),
        (x, y+1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1),
    ]

    for i, j in coordinates:
        try:
            if i < 0 or j < 0: continue
            neighbors.append(array[i][j])
        except IndexError: ...

    return neighbors.count(1)


def is_inside(array, x, y):
    """Will check if element (x, y) is inside the grid."""
    try: _ = array[x][y]
    except IndexError: return False
    return True
