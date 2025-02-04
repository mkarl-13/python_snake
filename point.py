class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, val):
        return Point(self.x + val.x, self.y + val.y)
    def __mul__(self, val):
        return Point(self.x * val, self.y * val)
    def __eq__(self, other):
        if isinstance(other, Point):
            if (other.x == self.x and other.y == self.y):
                return True
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
