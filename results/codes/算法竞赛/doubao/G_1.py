n, m, q = map(int, input().split())

# 构建邻接表
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# 初始化每个建筑上方的积雨云数量
clouds = [0] + [int(input()) for _ in range(n)]

# 处理事件
for _ in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        x, v = event[1], event[2]
        clouds[x] += v
    else:
        x = event[1]
        total = 0
        for neighbor in adj[x]:
            total += clouds[neighbor]
        print(total)