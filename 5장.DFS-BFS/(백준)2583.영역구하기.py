# https://www.acmicpc.net/problem/2583
from collections import deque

M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    count = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
        if nx >= 0 and ny >= 0 and nx < N and ny < M and graph[ny][nx]==0:
            graph[ny][nx] = 1
            q.append((ny, nx))
            count += 1
    return count

result = []
print(graph)
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] += 1
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))
