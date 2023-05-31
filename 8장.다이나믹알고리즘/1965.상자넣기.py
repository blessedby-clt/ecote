# 링크:https://www.acmicpc.net/problem/1965

N = int(input())
box_list = list(map(int, input().split()))

d = [1] * 1001
for i in range(1, N):
    if box_list[i] > box_list[i-1]:
        d[i+1] = d[i] + 1
    else:
        if i == 1:
            d[i+1] = 1
        else:
            if box_list[i] > box_list[i-2]:
                d[i+1] = d[i]
            else:
                d[i+1] = d[i] - 1
print(max(d))
