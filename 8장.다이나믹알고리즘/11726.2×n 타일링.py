# 링크 : https://www.acmicpc.net/problem/11726
N = int(input())
d = [1] * 1001

for i in range(2, N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N] % 10007)

