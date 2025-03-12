from utils.problem_utils import read_data, write_answer
from models.problem import Problem

input_path = "data/input2.txt"
output_path = "data/output.txt"

criteria, goal_function = read_data(input_path)
problem = Problem(criteria, goal_function)

result = problem.solve()
write_answer(output_path, result)