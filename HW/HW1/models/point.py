# import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return "({.f4}, {.f4})".format(self.x, self.y)
    
    # def distance(self, other: "Point"):
    #     dx = self.x - other.x
    #     dy = self.y - other.y
    #     return math.sqrt(dx**2 + dy**2)
