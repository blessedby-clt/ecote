import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
# visit_graph = [[False]*n for i in range(n)]

map_graph = []
for i in range(n):
    map_graph.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#
max_height = 0
for i in map_graph:
    temp_max = max(i)
    if max_height < temp_max:
        max_height = temp_max

def dfs(r, c, h):
    visit_graph[r][c] = True
    if map_graph[r][c] > h:
        safe_ground.append((r, c))
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if visit_graph[nx][ny] == False:
                    dfs(nx, ny, h)

answer = 1
for height in range(1, max_height+1):
    result = 0
    safe_ground = []
    visit_graph = [[False] * n for i in range(n)]
    for r in range(n):
        for c in range(n):
            if visit_graph[r][c] == False:
                dfs(r, c, height)
                if len(safe_ground) > 0:
                    result += 1
                    safe_ground = []
    # print(height, ":", result)
    if answer < result:
        answer = result

print(answer)