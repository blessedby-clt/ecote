import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

INF = int(1e9)
v, e = map(int, input().split())
start = int(input())

graph = [[] for i in range(v+1)]
distance = [INF]*(v+1)

for i in range(e):
    x, city, dist = map(int, input().split())
    graph[x].append((city, dist))

def daikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

daikstra(start)
for dist in distance[1:]:
    if dist >= INF:
        print('INF')
    else:
        print(dist)