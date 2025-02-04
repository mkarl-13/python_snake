import pygame
from settings import DEFAULT_SNAKE, DEFAULT_COLORS, GRID_SIZE, CELL_SIZE
from point import Point

class Snake:
    def __init__(self, food):
        self.pos = DEFAULT_SNAKE["pos"]
        self.dir = DEFAULT_SNAKE["dir"]
        self.length = DEFAULT_SNAKE["length"]
        self.segments = []
        self.food = food

    def Reset(self):
        self.pos = DEFAULT_SNAKE["pos"]
        self.dir = DEFAULT_SNAKE["dir"]
        self.length = DEFAULT_SNAKE["length"]
        self.segments = []
        self.food.Move(self.pos, self.segments)
    
    def Input(self, key):
        if key == pygame.K_q:
            self.dir = Point(-1, 0)
        if key == pygame.K_d:
            self.dir = Point(1, 0)
        if key == pygame.K_z:
            self.dir = Point(0, -1)
        if key == pygame.K_s:
            self.dir = Point(0, 1)

    def OnTick(self):
        self.Move()
        self.CheckFood()
        self.CheckCollision()

    def Render(self, surf):
        for segment in self.segments:
            pygame.draw.rect(surf, DEFAULT_COLORS["body"], (segment.x * CELL_SIZE.x, segment.y * CELL_SIZE.y, CELL_SIZE.x, CELL_SIZE.y))
        pygame.draw.rect(surf, DEFAULT_COLORS["head"], (self.pos.x * CELL_SIZE.x, self.pos.y * CELL_SIZE.y, CELL_SIZE.x, CELL_SIZE.y))
        return
    
    def Move(self):
        self.segments.append(Point(self.pos.x, self.pos.y))
        self.pos += self.dir
        if len(self.segments) > self.length:
            self.segments.pop(0)
        return
    
    def CheckFood(self):
        if self.pos == self.food.pos:
            self.length += 1
            self.food.Move(self.pos, self.segments)
        return
    
    def CheckCollision(self):
        if self.dir != Point(0, 0):
            for segment in self.segments:
                if segment == self.pos:
                    self.Reset()
            if self.pos.x > GRID_SIZE.x - 1  or self.pos.y > GRID_SIZE.y - 1:
                self.Reset()
            if self.pos.x < 0  or self.pos.y < 0:
                self.Reset()
        return