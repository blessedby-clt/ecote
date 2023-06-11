INF = int(1e9)
# 도시개수
n = int(input())

# 버스 개수
m = int(input())

# 최단거리 경로 테이블
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    if graph[x][y] > z:
        graph[x][y] = z

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for start in graph[1:]:
    for dist in start[1:]:
        if dist >= INF:
            print(0, end = ' ')
        else:
            print(dist, end = " ")
    print()


