from collections import deque

graph = []
data = []

for i in range(3):
    graph.append(list(map(int, input().split())))
    for j in range(3):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
data.sort()
# 1 0 2
# 0 0 0
# 3 0 0

q = deque(data)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, time, x, y = q.popleft()
    if time == 2:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 3 and ny >= 0 and ny < 3:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))

print(graph)