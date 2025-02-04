from point import Point
import random
import pygame
from settings import GRID_SIZE, CELL_SIZE
from colors import DEFAULT_COLORS

class Food:
    pos = Point(0, 0)
    def Move(self, head, body):
        x = random.randint(0, GRID_SIZE.x - 1)
        y = random.randint(0, GRID_SIZE.y - 1)
        if x == head.x and y == head.y:
            return self.Move(head, body)
        for segment in body:
            if segment.x == x and segment.y == y:
                return self.Move(head, body)
        self.pos = Point(x, y)
        return
    def Render(self, surf, colors):
        pygame.draw.rect(surf, colors[DEFAULT_COLORS["FOOD"]], (self.pos.x * CELL_SIZE.x, self.pos.y * CELL_SIZE.y, CELL_SIZE.x, CELL_SIZE.y))
    