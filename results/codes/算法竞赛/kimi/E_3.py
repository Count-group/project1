import random

def calculate_probability(n, A, p):
    def calculate_S(A, p):
        S = []
        for i in range(n):
            S_i = [0, 0, 0]
            for j in range(3):
                for k in range(3):
                    S_i[j] += p[i][k] * A[j][k]
            S.append(S_i)
        return S

    def is_valid(q, S):
        for i in range(n):
            if q[0] * S[i][0] + q[1] * S[i][1] + q[2] * S[i][2] < 0:
                return False
        return True

    # Calculate S for each game
    S = calculate_S(A, p)

    # Monte Carlo method to estimate the probability
    total_samples = 10**6
    valid_samples = 0

    for _ in range(total_samples):
        q1 = random.uniform(0, 1)
        q2 = random.uniform(0, 1 - q1)
        q3 = 1 - q1 - q2
        if is_valid([q1, q2, q3], S):
            valid_samples += 1

    return valid_samples / total_samples

# 输入部分
n = int(input())
A = [list(map(int, input().split())) for _ in range(3)]
p = [list(map(float, input().split())) for _ in range(n)]

# 计算结果
result = calculate_probability(n, A, p)
print(f"{result:.6f}")