# [EX1] SOLVE SYSTEM OF IN-EQUATION
## Problem definition

Write function that read input data follow the format:
- $M$ constraints $(0 < M \le 50)$
- Each constraint has the form: $$a_i x_1 + b_i x_2 \le c_i$$
- The objective function: $$f(x_1, x_2)=c_1x_1 + c_2x_2 \ (x_1,x_2 \ge0)$$
- The whole values is in $[-50,50]$

Perform the following tasks:
- Find the extreme points
- The feasible range is bounded?
- $\min f$ and $\max f$ (can be not exist)

## Main idea
### Task 1 - Find extreme points
- **Step 1 - Find extreme points**: find all the intersections among lines. Extreme points are which satisfy all criteria
- **Step 2 - Check feasible range's boundedness**
- Step 3 - Check if maximun and mininum value of objective function exist and calculate them
### Task 2 - Check the boundedness of the feasible range
UPDATE LATER
### Task 3 - Calculate the $\min$ and $\max$ of the objective function
UPDATE LATER

## Local run
### Prepare input
- Create folder `data\`
- Place the input data in file `.txt`. For example, `intput.txt`
- Place the file path in varibale `input_path` and `output_path` in file `main.py`
### Run code
```bash
python3 main.py
```
### Check the answer
Check the algorithm's output in the file path `output_path` you have determine in `main.py`


## Example
| input | output|
|-------|-------|
|$3 \newline 1 \ 1\ 5 \newline 0 \ 1\ 2 \newline 1\ 2\ 6 \newline 30\ 50$ | $\text{1) Danh sach cac diem cuc bien la: (0, 0), (5, 0), (4,1), (2,2), (0,2)} \newline \text{2) Mien rang buoc la bi chan} \newline \text{3) GTLN la } F=190 \text{ tai } (4, 1) \newline \text{GTNN la } F=0 \text{ tai } (0,0)$ |
|||
