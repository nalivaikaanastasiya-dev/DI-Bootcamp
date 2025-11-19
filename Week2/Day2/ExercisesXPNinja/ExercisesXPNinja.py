import time
import os

class GameOfLife:
    def __init__(self, rows, cols, initial_state):
        self.rows = rows
        self.cols = cols
        self.grid = initial_state

    def _get_neighbors(self, r, c):
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                
                nr, nc = r + i, c + j
                
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.grid[nr][nc] == 1:
                        live_neighbors += 1
        return live_neighbors

    def next_generation(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self._get_neighbors(r, c)
                current_state = self.grid[r][c]

                if current_state == 1:
                    if live_neighbors < 2:
                        new_grid[r][c] = 0
                    elif live_neighbors == 2 or live_neighbors == 3:
                        new_grid[r][c] = 1
                    elif live_neighbors > 3:
                        new_grid[r][c] = 0
                else:
                    if live_neighbors == 3:
                        new_grid[r][c] = 1

        self.grid = new_grid

    def display_grid(self, generation):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Generation: {generation}")
        for row in self.grid:
            print(' '.join(['█' if cell == 1 else '░' for cell in row]))
        print("-" * (self.cols * 2))

class Simulation:
    def __init__(self, game, max_generations=100, delay=0.2):
        self.game = game
        self.max_generations = max_generations
        self.delay = delay
        self.history = []

    def run(self):
        generation = 0
        while generation < self.max_generations:
            
            current_state_tuple = tuple(tuple(row) for row in self.game.grid)
            if current_state_tuple in self.history:
                print("Game stabilized or entered a cycle.")
                break
            self.history.append(current_state_tuple)

            self.game.display_grid(generation)
            self.game.next_generation()
            generation += 1
            time.sleep(self.delay)
            
        else:
            self.game.display_grid(generation)
            print("Maximum generations reached.")

glider_state = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

blinker_state = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

pentadecathlon_state = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print("--- Starting Glider Simulation ---")
ROWS_1, COLS_1 = 10, 10
game1 = GameOfLife(ROWS_1, COLS_1, [[0] * COLS_1 for _ in range(ROWS_1)])
for r in range(5):
    for c in range(5):
        game1.grid[r + 1][c + 1] = glider_state[r][c]

sim1 = Simulation(game1, max_generations=50, delay=0.1)
sim1.run()

time.sleep(3)

print("--- Starting Blinker Simulation ---")
ROWS_2, COLS_2 = 10, 10
game2 = GameOfLife(ROWS_2, COLS_2, [[0] * COLS_2 for _ in range(ROWS_2)])
for r in range(5):
    for c in range(5):
        game2.grid[r + 3][c + 3] = blinker_state[r][c]

sim2 = Simulation(game2, max_generations=10, delay=0.5)
sim2.run()

time.sleep(3)

print("--- Starting Pentadecathlon Simulation ---")
ROWS_3, COLS_3 = 15, 15
game3 = GameOfLife(ROWS_3, COLS_3, [[0] * COLS_3 for _ in range(ROWS_3)])
for r in range(len(pentadecathlon_state)):
    for c in range(len(pentadecathlon_state[0])):
        game3.grid[r + 4][c + 2] = pentadecathlon_state[r][c]

sim3 = Simulation(game3, max_generations=30, delay=0.3)
sim3.run()