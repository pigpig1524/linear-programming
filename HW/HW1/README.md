# [EX1] SOLVE SYSTEM OF IN-EQUATION
## Student information
- **Full name:** Van Tuan Kiet
- **Student ID:** 22120177
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
- Find all the intersections of each pair of lines
- Loop through the set of intersections, the point satisfy all criteria is an extreme point
### Task 2 - Check the boundedness of the feasible range
For each extreme points $E$, loop through the lines it is in:
- Let $\vec{a}$ be the direction vector of the line
- Move point $E$ along the line (both side) infinitely far away
- If it still satisfy all criteria, then the feasible range is unbounded.

Loop for all lines, all extreme points to make sure we do not skip any case
### Task 3 - Calculate the $\min$ and $\max$ of the objective function
- Let $d, D$ be the minimum, maximum value of the list of objective functions's value at extreme points

For each loop iteration in the step two, when move the point $E$ far away. If it still satisfy all criteria, we calculate the value of objective function as well. 
- If it increase and greater than $D$, objective function does not have maximum value. 
- If it decrease and less than $d$, objective function does not have minimum value
## Local run
### Prepare input
- Create folder `data\`
- Place the input data in file `.txt`. For example, `intput_01.txt`
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
