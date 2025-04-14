import pygame
import random

# Constants
GRID_SIZE = (10, 10)  # Rows x Columns
BOMB_PROB = 0.15  # Probability of a bomb
TILE_SIZE = 50
SCREEN_SIZE = (GRID_SIZE[1] * TILE_SIZE, GRID_SIZE[0] * TILE_SIZE)

# Colors
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = pygame.font.Font(None, 36)

class Tile:
    def __init__(self, has_bomb):
        self.has_bomb = has_bomb
        self.revealed = False
        self.flagged = False
        self.neighbors = []
        self.bomb_count = 0

    def reveal(self):
        if not self.flagged:
            self.revealed = True
            if self.bomb_count == 0:
                for neighbor in self.neighbors:
                    if not neighbor.revealed:
                        neighbor.reveal()

    def toggle_flag(self):
        if not self.revealed:
            self.flagged = not self.flagged

class Minesweeper:
    def __init__(self, size, bomb_prob):
        self.rows, self.cols = size
        self.grid = [[Tile(random.random() < bomb_prob) for _ in range(self.cols)] for _ in range(self.rows)]
        self.set_neighbors()
        self.set_bomb_counts()
        self.game_over = False
        self.won = False

    def set_neighbors(self):
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = []
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            neighbors.append(self.grid[nr][nc])
                self.grid[r][c].neighbors = neighbors

    def set_bomb_counts(self):
        for row in self.grid:
            for tile in row:
                tile.bomb_count = sum(1 for neighbor in tile.neighbors if neighbor.has_bomb)

    def reveal_tile(self, row, col):
        if self.game_over or self.grid[row][col].flagged:
            return
        self.grid[row][col].reveal()
        if self.grid[row][col].has_bomb:
            self.game_over = True
        elif all(tile.revealed or tile.has_bomb for row in self.grid for tile in row):
            self.won = True

    def toggle_flag(self, row, col):
        if not self.game_over:
            self.grid[row][col].toggle_flag()

    def draw(self):
        screen.fill(WHITE)
        for r, row in enumerate(self.grid):
            for c, tile in enumerate(row):
                x, y = c * TILE_SIZE, r * TILE_SIZE
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, GRAY if tile.revealed else WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)

                if tile.revealed:
                    if tile.has_bomb:
                        pygame.draw.circle(screen, RED, (x + TILE_SIZE // 2, y + TILE_SIZE // 2), TILE_SIZE // 4)
                    elif tile.bomb_count > 0:
                        text = font.render(str(tile.bomb_count), True, BLACK)
                        screen.blit(text, (x + TILE_SIZE // 3, y + TILE_SIZE // 4))
                elif tile.flagged:
                    pygame.draw.polygon(screen, RED, [(x + 10, y + 40), (x + 25, y + 10), (x + 40, y + 40)])

        if self.game_over:
            text = font.render("Game Over!", True, RED)
            screen.blit(text, (SCREEN_SIZE[0] // 3, SCREEN_SIZE[1] // 3))
        elif self.won:
            text = font.render("You Win!", True, RED)
            screen.blit(text, (SCREEN_SIZE[0] // 3, SCREEN_SIZE[1] // 3))

        pygame.display.flip()

def main():
    game = Minesweeper(GRID_SIZE, BOMB_PROB)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not (game.game_over or game.won):
                x, y = event.pos
                row, col = y // TILE_SIZE, x // TILE_SIZE
                if event.button == 1:  # Left click to reveal
                    game.reveal_tile(row, col)
                elif event.button == 3:  # Right click to flag
                    game.toggle_flag(row, col)
        
        game.draw()

    pygame.quit()

if __name__ == "__main__":
    main()
