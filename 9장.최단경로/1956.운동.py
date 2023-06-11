import sys
input = sys.stdin.readline

INF = int(1e9)
# 마을 개수, 경로 개수
V, E = map(int, input().split())
# 경로 그래프
graph = [[INF]*(V+1) for _ in range(V+1)]

for i in range(E):
    x, y, z = map(int, input().split())
    graph[x][y] = z

min_distance = INF
for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]

for i in range(1, V+1):
    min_distance = min(min_distance, graph[i][i])
if min_distance >= INF:
    print(-1)
else:
    print(min_distance)

## 시간초과 안 뜨게 하는 코드
# 링크: https://velog.io/@nkrang/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1956-%EC%9A%B4%EB%8F%99-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import heapq as hq

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
# 거리를 저장할 배열을 2차원으로
dist = [[1e9] * (V + 1) for _ in range(V + 1)]

heap = []
for _ in range(E):
    x, y, c = map(int, input().split())
    graph[x].append([c, y])
    dist[x][y] = c
    # heap에도 비용, 출발지, 도착지 3개의 값을 넣어준다.
    # 유효한 경로 값을 다 넣어줌
    hq.heappush(heap, [c, x, y])

while heap:
    # 최소 비용의 경로를 먼저 뽑아주고 (d:비용, s:출발, g:도착)
    d, s, g = hq.heappop(heap)
    # 출발지와 도착지가 같다면 사이클!
    # heap을 이용하기 때문에 처음 나온 사이클이 가장 비용이 작은 사이클이므로 break 해버려도 됨! -> 여기서 시간이 굉장히 절약되는 듯
    if s == g:
        print(d)
        break
    # d 값이 이미 저장된 비용보다 크다면 넘겨버림
    if dist[s][g] < d:
        continue

    # g에서 갈 수 있는 노드들을 검사
    for nd, ng in graph[g]:
        # s->g->ng로 가는 비용
        new_d = d + nd
        # s->g->ng로 가는게 s->ng보다 빠르다면 값 갱신해주고 heap에 넣어줌
        if new_d < dist[s][ng]:
            dist[s][ng] = new_d
            hq.heappush(heap, [new_d, s, ng])
else:
    # heap 다 돌았는데 없다면 -1
    print(-1)