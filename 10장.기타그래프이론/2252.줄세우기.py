# 링크 : https://www.acmicpc.net/problem/2252

from collections import deque
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

v, e = map(int, input().split())

indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]
result = []

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for student in graph[now]:
            indegree[student] -= 1

            if indegree[student] == 0:
                q.append(student)

topology_sort()
for j in result:
    print(j, end = " ")