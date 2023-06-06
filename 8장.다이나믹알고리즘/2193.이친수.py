# 링크 : https://www.acmicpc.net/problem/2193

N = int(input())

d = [0]*100
d[1] = 1
for i in range(2, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])
