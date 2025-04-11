from pydantic import BaseModel
from typing import Optional
import numpy as np
from tabulate import tabulate


class Problem:
    def __init__(self,
                 criteria_coeffs: np.array,
                 target: np.array,
                 objective_coeffs: np.array,
                 operator: np.array):
        pass
        self.criteria_coeffs = criteria_coeffs
        self.target = target
        self.objective_coeffs = objective_coeffs
        self.operator = operator
        self.base_coeffs = None
        self.base_values = None
        self.base_index = None
        # self.overall = None
        # self.deltas = None
        self.initial_table = None

    def calc_initial_table(self):
        overall = self.base_coeffs @ self.base_values
        deltas = self.base_coeffs @ self.criteria_coeffs - self.objective_coeffs
        # return overall, deltas
        x_label = [f"x{idx:.0f}" for idx in self.base_index]

        data = np.concatenate(
            [
                np.concatenate([x_label, [""]]).reshape(-1, 1),
                np.concatenate([self.base_coeffs, [""]]).reshape(-1, 1),
                np.concatenate([self.base_values, [overall]]).reshape(-1, 1),
                np.concatenate([self.criteria_coeffs, [deltas]])
            ],
            axis=1
        )
        self.initial_table = tabulate(data, tablefmt="grid")

    def __str__(self):
        # result = ""
        # for key, value in self.__dict__.items():
        #     result += f"{key}:\n{value}\n\n"
        # return result.strip()
        return str(self.initial_table)