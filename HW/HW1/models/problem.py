from models.inequation import Inequation
from models.equation import CannotSolveException
from models.point import Point
from models.function import Function
import numpy as np

STEP = 10**9

class Problem:
    """
    The problem is to solve the following requirements of a system of in-equations:
        1. Find the extreme points
        2. The criteria range is open or not?
        3. Find max/min of the goal function (it can be null)
    Each in-equation in the system is in the form of ax + by <= c. We can consider as f(x,y) <= target
    """
    def __init__(self, criteria, goal_function):
        self.criteria : list[Inequation] = criteria
        self.goal_func : Function = goal_function
        self.extreme_points : set[Point] = set()
        self.objective_values : list = []
        self.is_bounded : bool = True
        self.exist_max = True
        self.exist_min = True

    def __str__(self):
        return "\n".join([str(x) for x in self.criteria])

    def is_satisfied(self, point: Point):
        for ieq in self.criteria:
            if not ieq.check_criteria(point):
                return False
        return True

    def find_extreme_points(self):
        n = len(self.criteria)
        for i in range(n - 1):
            for j in range(i + 1, n):
                try:
                    intersecttion = self.criteria[i].find_intersection(self.criteria[j])
                    self.extreme_points.add(intersecttion)
                except CannotSolveException:
                    continue
        for point in list(self.extreme_points):
            if not self.is_satisfied(point):
                self.extreme_points.remove(point)
                continue
            self.objective_values += [self.goal_func.calculate(point)]

    def check_boundedness(self):
        if len(self.extreme_points) == 0:
            self.exist_max = False
            self.exist_min = False
            self.is_bounded = False
            return

        for point in self.extreme_points:
            for ieq in self.criteria:
                if not ieq.is_inline(point):
                    continue
                vector = ieq.direction_vector
                if vector.prod() < 0:
                    break
                if vector[0] * point.x < 0:
                    vector *= -1
                vector *= STEP
                temp = Point(point.x + vector[0], point.y + vector[1])
                # print("Diem test: ", point, vector, " = ", temp)
                if self.is_satisfied(temp):
                    self.is_bounded = False
                    # print("Khong bi chan")
                    temp_value = self.goal_func.calculate(temp)
                    dist = self.goal_func.calculate(point) - temp_value
                    if dist > 0 and temp_value < min(self.objective_values):
                        self.exist_min = False
                    elif dist < 0 and temp_value > max(self.objective_values):
                        self.exist_max = False
        
    def solve(self):
        # task 1
        self.find_extreme_points()
        task1_res = "Danh sach cac diem cuc bien la:\n"
        for point in self.extreme_points:
            task1_res += "\t{}".format(str(point))

        # Task 2
        task2_res = "Mien rang buoc "
        self.check_boundedness()
        if self.is_bounded:
            task2_res += "la bi chan"
        else:
            task2_res += "khong bi chan"

        # Task 3
        task3_res = ""
        temp = np.array(self.objective_values)
        if self.exist_max:
            task3_res += "GTLN la {} tai diem {}\n".format(
                temp.max(),
                list(self.extreme_points)[temp.argmax()]
            )
        else:
            task3_res += "Khong ton tai GTLN\n"
        if self.exist_min:
            task3_res += "GTNN la {} tai diem {}".format(
                temp.min(),
                list(self.extreme_points)[temp.argmin()]
            )
        else:
            task3_res += "Khong ton tai GTNN"
        del temp
        return "1) {}\n2) {}\n3) {}".format(task1_res,
                                            task2_res,
                                            task3_res)