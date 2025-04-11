from solver import Solver
import os
from tqdm import tqdm

INPUT_DIR = 'data/input'
OUTPUT_DIR = 'data/output'
solver = Solver()


if __name__ == '__main__':
    files = os.listdir(INPUT_DIR)
    for file in tqdm(files):
        input_filepath = os.path.join(INPUT_DIR, file)
        output_name = file.replace('input', 'output')
        output_filepath = os.path.join(OUTPUT_DIR, output_name)

        solver.input_data(input_filepath)
        solver.solve()
        solver.write_answer(output_filepath)
