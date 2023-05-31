# 링크 : https://www.acmicpc.net/problem/9095
T = int(input())
number_list = []
for _ in range(T):
     number_list.append(int(input()))

d = [0] * 1001
d[1] = 1
d[2] = 2
d[3] = 4

for j in range(4, max(number_list)+ 1):
    d[j] = d[j-1] + d[j-2] + d[j-3]

for number in number_list:
    print(d[number])


