n = int(input())
visit_graph = [[False]*n for i in range(n)]
map_graph = []
for i in range(n):
    map_graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(r, c, n):
    visit_graph[r][c] = True
    if map_graph[r][c] > n :
        safe_ground.append((r, c))
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if visit_graph[nx][ny] == False:
                    dfs(nx, ny, n)

result = 0
safe_ground = []
for r in range(n):
    for c in range(n):
        if visit_graph[r][c] == False:
            dfs(r, c, n)
            if len(safe_ground) > 0:
                result += 1
                safe_ground = []

print(result)
