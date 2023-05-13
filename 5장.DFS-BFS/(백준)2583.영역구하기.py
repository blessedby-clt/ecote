# https://www.acmicpc.net/problem/2583
from collections import deque

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            graph[i][j] += 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j, count):
    q = deque()
    q.append((i, j))
    while q:
        y, x = q.popleft()
        count += 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if nx >= 0 and ny >= 0 and nx < N and ny < M and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx))

    return count


result = []
for i in range(M):
    for j in range(N):
        count = 0
        if graph[i][j] == 0:
            graph[i][j] += 1
            count = bfs(i, j, count)
            result.append(count)


print(len(result))
print(*sorted(result))
