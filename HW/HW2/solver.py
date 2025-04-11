from problem import Problem
import numpy as np
from utils import load_data, write_answer

M = 1000

class Solver:
    def __init__(self):
        self.problem = None
        self.processed = False

    def input_data(self, file_path):
        criteria_coeffs, target, objective_coeffs, operator = load_data(file_path)
        self.problem = Problem(criteria_coeffs, target, objective_coeffs, operator)
        self.processed = False

    def standardize(self):
        d = len(self.problem.operator)
        adds = np.zeros((d, d))
        np.fill_diagonal(adds, self.problem.operator)
        adds = adds[:, ~np.all(adds == 0, axis=0)]
        self.problem.operator *= 0
        self.problem.objective_coeffs = np.concatenate([self.problem.objective_coeffs,
                                                        np.zeros(adds.shape[1])])
        self.problem.criteria_coeffs = np.concatenate([self.problem.criteria_coeffs, adds], axis=1)
        
        idx = np.argwhere(self.problem.target.flatten() < 0).flatten()
        self.problem.criteria_coeffs[idx] *= -1
        self.problem.target[idx] *= -1


    def detect_base_variables(self):
        self.problem.base_coeffs = np.zeros(len(self.problem.criteria_coeffs))
        self.problem.base_index = np.zeros(len(self.problem.criteria_coeffs))
        self.problem.base_values = np.zeros(len(self.problem.criteria_coeffs))
        # row_index = []
        for i in range(self.problem.criteria_coeffs.shape[1]):
            col = self.problem.criteria_coeffs[:, i]
            row = np.argwhere(col != 0).flatten()
            if len(row) == 1:
                row = row[0]
                num = col[row]
                value = self.problem.target[row][0]
                if num * value >= 0:
                    # base.append(num)
                    if num != 1:
                        self.problem.criteria_coeffs[row] /= num
                        self.problem.target[row] /= num
                    if num < 0:
                        self.problem.criteria_coeffs[row] *= -1
                        self.problem.target[row] *= -1

                    self.problem.base_coeffs[row] = self.problem.objective_coeffs[i]
                    self.problem.base_index[row] = i + 1
                    self.problem.base_values[row] = self.problem.target[row][0]
                    continue

    def add_big_M(self):
        need_fill_index = np.argwhere(self.problem.base_index == 0)
        new_coeffs = np.zeros_like(self.problem.base_coeffs)
        new_coeffs[need_fill_index] = 1
        adds = np.zeros((len(self.problem.operator), len(self.problem.operator)))
        np.fill_diagonal(adds, new_coeffs)

        adds = adds[:, ~np.all(adds == 0, axis=0)]
        self.problem.criteria_coeffs = np.concatenate(
            [
                self.problem.criteria_coeffs,
                adds
            ],
            axis=1
        )

        self.problem.objective_coeffs = np.concatenate(
            [
                self.problem.objective_coeffs,
                [-M] * len(need_fill_index)
            ],
            axis=0
        )

        need_fill_index = need_fill_index.flatten()
        self.problem.base_coeffs[need_fill_index] = -M
        n = self.problem.criteria_coeffs.shape[1]
        self.problem.base_index[need_fill_index] = np.arange(-len(need_fill_index), 0) + n + 1
        self.problem.base_values[need_fill_index] = self.problem.target[need_fill_index].flatten()

    def calculate_initial_table(self):
        # overall, deltas = self.problem.calc_initial_table()
        self.problem.calc_initial_table()

    def solve(self):
        if not self.problem:
            raise ValueError("Data not found")
        self.standardize()
        self.detect_base_variables()
        self.add_big_M()
        self.calculate_initial_table()
        self.processed = True

    def write_answer(self, output_path: str):
        if not self.processed:
            raise ValueError("Problem has not been solved")
        write_answer(output_path, str(self.problem))
        