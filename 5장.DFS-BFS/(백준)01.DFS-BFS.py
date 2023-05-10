# 문제 링크
# https://www.acmicpc.net/problem/1260

# Input
# 4 5 1  Node 개수, Edge 개수, 최초 시작점
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# OUTPUT
# 1 2 4 3  DFS 결과
# 1 2 3 4  BFS 결과

from collections import deque

n, m, start_number = map(int, input().split())
edge_node_list = []
for i in range(m):
    edge_node_list.append(list(map(int, input().split())))
graph_list = []
for index in range(n+1):
    graph_list.append([])
for element in edge_node_list:
    graph_list[element[0]].append(element[1])
    graph_list[element[1]].append(element[0])


dfs_result = []
bfs_result = []
queue = deque()
visit_list = [False for _ in range(n+1)]
def dfs(i):
    visit_list[i] = True
    dfs_result.append(i)
    temp = sorted(graph_list[i])
    for number in temp:
        if visit_list[number] == False:
            dfs(number)

def bfs(i):
    queue.append(i)
    visit_list[i] = True
    while queue:
        element = queue.popleft()
        bfs_result.append(element)
        temp = sorted(graph_list[element])
        for number in temp:
            if visit_list[number] == False:
                queue.append(number)
                visit_list[number] = True
#
#
dfs(start_number)
visit_list = [False for _ in range(n+1)]
bfs(start_number)

print(" ".join(map(str,dfs_result)))
print(" ".join(map(str,bfs_result)))