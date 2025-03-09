# from models.equation import Equation
from utils.problem_utils import read_data
from models.problem import Problem

input_path = "data/input.txt"
output_path = "data/output.txt"

criteria, goal_function = read_data(input_path)
problem = Problem(criteria, goal_function)

problem.solve()