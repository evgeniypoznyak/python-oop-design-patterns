from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        obj = deepcopy(self)
        obj.move(move_x, move_y)
        return obj


point1 = Point(0, 0)
print(point1)

point2 = point1.clone(1, 1)
print(point2)
