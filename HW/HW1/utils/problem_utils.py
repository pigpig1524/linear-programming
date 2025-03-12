from models.inequation import Inequation
from models.function import Function

def read_data(file_path):
    try:
        file = open(file_path, 'r')
    except Exception as e:
        print(f"File '{file_path}' doesn't exist")
        return None
    
    criteria = [
        Inequation(Function(0, -1), 0),
        Inequation(Function(-1, 0), 0)
    ]
    lines : list[str] = file.readlines()
    n = int(lines.pop(0).strip())
    for idx in range(n):
        tmp = lines[idx].strip().split(' ')
        criteria.append(Inequation(
            func=Function(int(tmp[0]), int(tmp[1])),
            target=int(tmp[2])
        ))
    tmp = lines[-1].strip().split(' ')
    goal_func = Function(int(tmp[0]), int(tmp[1]))
    return (criteria, goal_func)

def write_answer(file_path, content):
    f = open(file_path, 'w', encoding='utf-8')
    f.write(content)
    f.close()