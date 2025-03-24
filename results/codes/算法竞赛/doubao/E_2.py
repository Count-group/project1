import numpy as np
from scipy.integrate import dblquad


# Read the number of games
n = int(input())

# Read the matrix A
A = []
for _ in range(3):
    row = list(map(int, input().split()))
    A.append(row)
A = np.array(A)

# Read the probabilities of other robots
p = []
for _ in range(n):
    prob_row = list(map(float, input().split()))
    p.append(prob_row)


def expected_score(q1, q2):
    q3 = 1 - q1 - q2
    q = np.array([q1, q2, q3])
    for i in range(n):
        exp_val = 0
        for j in range(3):
            for k in range(3):
                exp_val += q[j] * p[i][k] * A[j][k]
        if exp_val < 0:
            return 0
    return 1


# Define the integration limits
# q1 ranges from 0 to 1
# For a fixed q1, q2 ranges from 0 to 1 - q1
result, _ = dblquad(expected_score, 0, 1, lambda x: 0, lambda x: 1 - x)
print("{:.6f}".format(result))