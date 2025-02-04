# Importing the pygame library.
import pygame

from snake import Snake
from food import Food
from palette_manager import PaletteManager
from grid import Grid
from colors import DEFAULT_COLORS

from settings import *
from palette_manager import *

def main():
    running = True
    
    # Initial pygame setup.
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE.x, WINDOW_SIZE.y))

    # Creates a grid object which will only be used to render the grid.
    grid = Grid()

    # Creates a palette manager object for colors management.
    palette_manager = PaletteManager()

    # Creates Food, snake and setup a reference to the Food in the snake.
    food = Food()
    snake = Snake(food)

    # Schedule an event fired on each game tick.
    GAME_TICK = pygame.USEREVENT + 0
    pygame.time.set_timer(GAME_TICK, TICK_DURATION)

    # Main loop
    while running:
    # Event loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == GAME_TICK:
                snake.OnTick()
            if event.type == pygame.KEYDOWN:
                snake.Input(event.key)
                if event.key == pygame.K_c:
                    palette_manager.SwitchPalette()

        # Clear screen
        screen.fill(palette_manager.colors[DEFAULT_COLORS["BACKGROUND"]])

        # Renders the Food and the Snake
        food.Render(screen, palette_manager.colors)
        snake.Render(screen, palette_manager.colors)
        grid.Render(screen, palette_manager.colors)

        # Displays everything (essentially flip the buffer).
        pygame.display.flip()
    return

if __name__ == "__main__": main()
pygame.quit()