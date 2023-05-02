from collections import deque

m = 4
n = 4
k = 2
x = 1
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    print(now)
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            print(q)
            print(distance)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단거리가 K인 도시가 없다면 -1 출력
if not check:
    print(-1)