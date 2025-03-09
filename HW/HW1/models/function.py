from models.point import Point

class Function:
    """
    The form of function is: f(x,y) = ax + by
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}x + {self.b}y"

    # def solve_equation(self, target):
    #     pass
    
    def calculate(self, point: Point):
        return self.a * point.x + self.b * point.y