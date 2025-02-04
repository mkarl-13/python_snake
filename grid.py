import pygame
from settings import GRID_SIZE, CELL_SIZE
from colors import DEFAULT_COLORS

class Grid:
    def Render(self, surf, colors):
        for x in range(GRID_SIZE.x):
            for y in range(GRID_SIZE.y):
                pygame.draw.rect(surf, colors[DEFAULT_COLORS["GRID"]], (x * CELL_SIZE.x, y * CELL_SIZE.y, CELL_SIZE.x, CELL_SIZE.y), 1)

