from utils.problem_utils import read_data, write_answer
from models.problem import Problem
import os


input_dir_path = "data/input/"
output_dir_path = "data/output/"


def main_process(input_path: str, output_path: str):
    criteria, goal_function = read_data(input_path)
    problem = Problem(criteria, goal_function)
    result = problem.solve()
    write_answer(output_path, result)


if __name__ == "__main__":
    for file in list(sorted(os.listdir(input_dir_path))):
        input_path = input_dir_path + file
        output_path = output_dir_path + f"output_{file.split('_')[-1]}"
        print("Input", input_path, "--->", "Output:", output_path)
        try:
            main_process(input_path, output_path)
        except Exception as e:
            print("ERROR: " + str(e))
            continue

