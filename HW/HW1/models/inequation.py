from models.equation import Equation
from models.point import Point
from typing import overload

class Inequation(Equation):
    """
    The form of an inequation is: ax + by <= c. We can consider as func(x, y) <= target
    """
    def __init__(self, func, target):
        super().__init__(func, target)
    
    def check_criteria(self, point: Point):
        return self.func.calculate(point) <= self.target
