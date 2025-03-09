# import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return "({:.4f}, {:.4f})".format(self.x, self.y)
    
    def standardize(self):
        if self.x == -0:
            self.x = 0
        if self.y == -0:
            self.y = 0
    
    # def distance(self, other: "Point"):
    #     dx = self.x - other.x
    #     dy = self.y - other.y
    #     return math.sqrt(dx**2 + dy**2)
