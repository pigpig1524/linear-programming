from models.inequation import Inequation
from models.equation import CannotSolveException
from models.point import Point

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
        self.goal_func = goal_function
        self.extreme_points : list[Point] = []
        self.max = None
        self.min = None

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
                    self.extreme_points.append(intersecttion)
                except CannotSolveException as e:
                    continue
        i = 0
        while i < len(self.extreme_points):
            if not self.is_satisfied(self.extreme_points[i]):
                self.extreme_points.pop(i)
                continue
            i += 1

        
    def solve(self):
        # task 1
        self.find_extreme_points()
        # for point in self.extreme_points:
        #     task1_res += "\t{}".format(str(point))