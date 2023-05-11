# 링크 : https://www.acmicpc.net/problem/2667
# INPUT
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# OUTPUT
# 3
# 7
# 8
# 9

n = int(input())
map_graph = []
for i in range(n):
    temp_list = []
    input_char = input()
    for char in input_char:
        temp_list.append(int(char))
    map_graph.append(temp_list)


visit_graph = [
    [False]*n for i in range(n)
]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []
print(map_graph)
print(visit_graph)

def dfs(r, c):
    if not visit_graph[r][c] and map_graph[r][c] == 1:
        visit_graph[r][c] = True

        temp_list.append((r, c))
        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if not visit_graph[nx][ny] and map_graph[nx][ny] == 1:
                    dfs(nx, ny)

for r in range(n):
    for c in range(n):
        temp_list = []
        dfs(r, c)
        if len(temp_list) > 0:
            answer.append(len(temp_list))

answer.sort()
print(len(answer))
print("\n".join(map(str,answer)))



