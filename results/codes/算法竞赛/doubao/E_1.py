import numpy as np
from scipy.integrate import dblquad


n = int(input())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
A = np.array(A)

p = []
for _ in range(n):
    p.append(list(map(float, input().split())))


def expected_score(q1, q2, p):
    q3 = 1 - q1 - q2
    q = np.array([q1, q2, q3])
    exp_scores = []
    for prob in p:
        exp_score = 0
        for i in range(3):
            for j in range(3):
                exp_score += q[i] * prob[j] * A[i][j]
        exp_scores.append(exp_score)
    return all(score >= 0 for score in exp_scores)


def integrand(q2, q1):
    return expected_score(q1, q2, p)


result, _ = dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1 - x)

print("{:.6f}".format(result))