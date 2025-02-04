from point import Point

GRID_SIZE = Point(21, 21)
CELL_SIZE = Point(30, 30)
WINDOW_SIZE = Point(GRID_SIZE.x * CELL_SIZE.x, GRID_SIZE.y * CELL_SIZE.y)
TICK_DURATION = 200

DEFAULT_SNAKE = {
    "pos": Point(int(GRID_SIZE.x/2), int(GRID_SIZE.y/2)),
    "dir": Point(0, 0),
    "length": 4
}