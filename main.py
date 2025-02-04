# Importing the pygame library.
import pygame

from snake import Snake
from food import Food

from settings import *
from colors import *

# Variables
running = True
    
# Initial pygame setup.
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE.x, WINDOW_SIZE.y))

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

    # Clear screen
    screen.fill(DEFAULT_COLORS["bg"])

    # Renders the Food and the Snake
    food.Render(screen)
    snake.Render(screen)

    # Renders a grid on top of everything.
    for x in range(GRID_SIZE.x):
        for y in range(GRID_SIZE.y):
            pygame.draw.rect(screen, DEFAULT_COLORS["grid"], (x * CELL_SIZE.x, y * CELL_SIZE.y, CELL_SIZE.x, CELL_SIZE.y), 1)

    # Displays everything (essentially flip the buffer).
    pygame.display.flip()
pygame.quit()