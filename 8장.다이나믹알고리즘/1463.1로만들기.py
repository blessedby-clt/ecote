# https://www.acmicpc.net/problem/1463

d = [0]*(int(1e6)+1)
N = int(input())

# d = [0]*11
# N = 10

d[1] = 0
for j in range(2, N+1):
    d[j] = d[j-1] + 1
    if j % 2 == 0:
        d[j] = min(d[j//2] + 1, d[j])
    if j % 3 == 0:
        d[j] = min(d[j//3] + 1, d[j])

print(d[N])


