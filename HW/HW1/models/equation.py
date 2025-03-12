from models.point import Point
from models.function import Function
from utils.model_utils import calc_det_equation
import numpy as np


class CannotSolveException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.msg = "[ERROR] Cannot find solution"

    def __str__(self):
        return self.msg


class Equation:
    """
    The equation's form is: ax + by = c. We can consider as func(x,y) = target
    """
    def __init__(self, func: Function, target: int):
        self.func = func
        self.target = target
        self.direction_vector = np.array([-self.func.b, self.func.a])

    def find_intersection(self, other: "Equation"):
        """
        This function solve the system of 2 equations. In this project's scope
        Args:
            other (Eqquation): the second equation
        Return
            root: Point
        """
        d, dx, dy = calc_det_equation(self.func, self.target, other.func, other.target)
        if d == 0:
            if dx == dy == 0:
                print("hai duong thang trung nhau")
            else:
                raise CannotSolveException()
        else:
            root = Point(dx/d, dy/d)
            root.standardize()
            return root
        
    def is_inline(self, point: Point):
        return self.func.calculate(point) == self.target
    
    def find_coordinate(self, x = None, y = None):
        if not x and not y:
            raise CannotSolveException()
        try:
            if x:
                x = (self.target - self.func.b * y) / self.func.a
            if y:
                y = (self.target - self.func.a * x) / self.func.b
            return Point(x, y)
        except Exception as e:
            raise CannotSolveException()