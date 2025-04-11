import numpy as np

def get_operator(text: str):
    ops_config = {"<=": 1, ">=": -1, '=': 0}
    for k, v in ops_config.items():
        if k in text:
            return (k, v)

def str_to_array(text: str):
    while '  ' in text:
        text = text.replace('  ', ' ')
    text = text.strip()
    return np.array([float(x) for x in text.split(' ')])

def read_file(file_path: str):
    lines = []
    with open(file_path, 'r') as f:
        for text in f.readlines():
            if text.strip() != '':
                lines += [text.strip()]
        f.close()
    return lines # 1 objective function and 2 criteria

def load_data(file_path: str):
    lines = read_file(file_path)
    objective_coeffs = str_to_array(lines[0])
    criteria_coeffs = []
    target = []
    operator = []

    for line in lines[1:]:
        ops, ops_value = get_operator(line)
        split = line.split(ops)
        operator += [ops_value]
        criteria_coeffs += [str_to_array(split[0])]
        target += [str_to_array(split[1])]
    criteria_coeffs = np.array(criteria_coeffs)
    target = np.array(target)
    operator = np.array(operator)
    
    return criteria_coeffs, target, objective_coeffs, operator

def write_answer(output_path, answer):
    with open(output_path, 'w') as f:
        f.write(answer)
        f.close()