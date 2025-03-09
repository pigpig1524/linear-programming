from models.inequation import Inequation
from models.point import Point

class Problem:
    def __init__(self, criteria, goal_function):
        self.criteria : list[Inequation] = criteria
        self.goal_func = goal_function
        self.extreme_points = []

    def find_extreme_points(self):
        pass