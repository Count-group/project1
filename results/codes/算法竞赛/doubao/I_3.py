# 手动实现全排列生成函数
def generate_permutations(arr):
    result = []
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
        for i in range(start, len(arr)):
            # 交换元素
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            # 回溯，恢复原顺序
            arr[start], arr[i] = arr[i], arr[start]
    backtrack(0)
    return result

# 读取输入
N, K, M = map(int, input().split())
intervals = []
for _ in range(M):
    l, r = map(int, input().split())
    intervals.append((l - 1, r - 1))

# 生成初始序列 A
A = list(range(1, K + 1)) + [0] * (N - K)
min_fine = float('inf')

# 生成所有排列
permutations = generate_permutations(A)
for perm in permutations:
    total_fine = 0
    for left, right in intervals:
        # 计算每个区间的最大值并累加到总罚款中
        total_fine += max(perm[left:right + 1])
    # 更新最小罚款
    min_fine = min(min_fine, total_fine)

print(min_fine)