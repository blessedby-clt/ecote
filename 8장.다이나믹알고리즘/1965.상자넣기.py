# 링크 : https://www.acmicpc.net/problem/1965
# 답안을 보고 작성. 추후 혼자 풀어보는 연습 필요.

N = int(input())
box_list = list(map(int, input().split()))

d = [1] * 1001
for i in range(1, N):
    for j in range(i):
        if box_list[i] > box_list[j]:
            d[i] = max(d[i], d[j]+1)
            print(d[i])

print(max(d))
