# Homework 2 - Initiate the simplex tableau with big-M
## Problem statement
Given a constraint system consisting of 2 conditions for a linear programming problem with 3 variables, and an objective function in maximization form – all input numbers are integers with absolute values not exceeding 10.

**Requirements**: Print out the initial simplex tableau using the Big-M method with the fewest number of artificial variables, where M = 1000

## Input, Output structure
### Input
* **Line 1:** $c_1, c_2, c_3$ are objective function coefficients
* **Line $i$ of 2 following lines:** $a_i, o_i, b_i$ are variables coeficients, operator, right-hand constant of the $i^{\text{th}}$ condition

**Note:** Operator can be `= <= >=`

## Example 
### Input
```plain
1 2 3
1 -1 2 = 3
3 4 -2 = 5
```
### Output
```plain
+----+---------+-------+-------+-------+----+---+---+
| x4 | -1000.0 |     3 |     1 |    -1 |  2 | 1 | 0 |
+----+---------+-------+-------+-------+----+---+---+
| x5 | -1000.0 |     5 |     3 |     4 | -2 | 0 | 1 |
+----+---------+-------+-------+-------+----+---+---+
|    |         | -8000 | -4001 | -3002 | -3 | 0 | 0 |
+----+---------+-------+-------+-------+----+---+---+
```
## Core ideas
* **Step 1:** Normalize the conditions
* **Step 2:** Find the existed base variables
* **Step 3:** Add artificial variables using big-M