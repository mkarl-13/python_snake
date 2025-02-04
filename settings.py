from colors import COLORS
from point import Point

GRID_SIZE = Point(21, 21)
CELL_SIZE = Point(30, 30)
WINDOW_SIZE = Point(GRID_SIZE.x * CELL_SIZE.x, GRID_SIZE.y * CELL_SIZE.y)
TICK_DURATION = 200

DEFAULT_COLORS = {
    "head": COLORS["4"],
    "body": COLORS["3"],
    "food": COLORS["6"],
    "grid": COLORS["1"],
    "bg": COLORS["0"]
}

DEFAULT_SNAKE = {
    "pos": Point(int(GRID_SIZE.x/2), int(GRID_SIZE.y/2)),
    "dir": Point(0, 0),
    "length": 4
}