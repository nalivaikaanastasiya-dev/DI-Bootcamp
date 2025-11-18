import math
import time
import os

# --- 1. Cell Class ---
class Cell:
    """Represents a single cell on the game grid."""
    def __init__(self, is_alive):
        self.is_alive = bool(is_alive)

    def __str__(self):
        # '█' for alive, '░' for dead
        return '█' if self.is_alive else '░'

# --- 2. GameOfLife Class ---
class GameOfLife:
    """Manages the game grid and the logic for generation transitions."""
    def __init__(self, initial_state):
        self.rows = len(initial_state)
        self.cols = len(initial_state[0])
        self.grid = self._initialize_grid(initial_state)

    def _initialize_grid(self, initial_state):
        """Converts the initial state (list of 0/1) into a grid of Cell objects."""
        grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                # Create a Cell object based on the initial state value
                row.append(Cell(initial_state[r][c]))
            grid.append(row)
        return grid

    def display(self):
        """Displays the current state of the grid."""
        # Clear the console for a smoother animation
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        print("-" * (self.cols * 2 + 1))
        for row in self.grid:
            print("|", end="")
            for cell in row:
                print(str(cell) + " ", end="")
            print("|")
        print("-" * (self.cols * 2 + 1))

    def count_live_neighbors(self, r, c):
        """Counts the number of live neighbors for the cell at (r, c)."""
        live_count = 0
        
        # Check all 8 surrounding positions
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the cell itself
                if dr == 0 and dc == 0:
                    continue
                
                neighbor_r, neighbor_c = r + dr, c + dc
                
                # Boundary Check: Fixed borders mean anything outside is considered dead
                is_in_bounds = (0 <= neighbor_r < self.rows) and \
                               (0 <= neighbor_c < self.cols)
                
                if is_in_bounds and self.grid[neighbor_r][neighbor_c].is_alive:
                    live_count += 1
        
        return live_count

    def next_generation(self):
        """Calculates and applies the rules for the transition to the next generation."""
        # Create a new grid to store the next state (crucial for simultaneous updates)
        new_grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                live_neighbors = self.count_live_neighbors(r, c)
                
                new_state = cell.is_alive # Default state is maintained
                
                # --- Rules of Life ---
                
                if cell.is_alive:
                    # 1. Underpopulation: Fewer than 2 live neighbors -> dies
                    if live_neighbors < 2:
                        new_state = False
                    # 2. Survival: 2 or 3 live neighbors -> lives on
                    # (new_state remains True)
                    # 3. Overpopulation: More than 3 live neighbors -> dies
                    elif live_neighbors > 3:
                        new_state = False
                else:
                    # 4. Reproduction: Exactly 3 live neighbors -> comes to life
                    if live_neighbors == 3:
                        new_state = True
                        
                # Store the new cell state in the next grid
                new_grid[r][c] = Cell(new_state)

        # Update the current grid with the newly calculated generation
        self.grid = new_grid


# --- Demonstration Run ---
if __name__ == "__main__":
    
    # 🌟 Initial State: Glider
    # A famous pattern that moves across the field
    glider_state = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    
    # 💥 Initial State: Blinker (Oscillator)
    blinker_state = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    # Select the initial setup by uncommenting one of the lines:
    initial_setup = glider_state
    # initial_setup = blinker_state
    
    game = GameOfLife(initial_setup)
    
    total_generations = 15
    print("🚀 Starting Conway's Game of Life...")

    for i in range(total_generations):
        game.display()
        print(f"\nGeneration: {i + 1} of {total_generations}")
        game.next_generation()
        time.sleep(0.3) # Delay for visualization
        
    print("\n--- Game Finished ---")