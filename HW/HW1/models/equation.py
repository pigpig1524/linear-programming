from models.point import Point
from models.function import Function
from utils.model_utils import calc_det_equation


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
        # self.a = a
        # self.b = b
        # self.c = c
        self.func = func
        self.target = target

    def find_intersection(self, other: "Equation"):
        """
        This function solve the system of 2 equations. In this project's scope, \
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


if __name__ == "__main__":
    x = Equation(1, 2)
    try:
        x.solve()
    except Exception as e:
        print(str(e))