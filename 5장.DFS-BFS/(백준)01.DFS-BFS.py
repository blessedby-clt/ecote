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

edge_node_list = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
graph_list = []
visit_list = []
for index in range(5):
    graph_list.append([])
    visit_list.append(False)
for element in edge_node_list:
    graph_list[element[0]].append(element[1])

dfs_result = []
bfs_result = []

def dfs(i):
    visit_list[i] = True
    dfs_result.append(i)
    for number in graph_list[i]:
        if visit_list[number] == False:
            dfs(number)

def bfs(i):
    pass




print(dfs(1))
print(dfs_result)
print(bfs(1))