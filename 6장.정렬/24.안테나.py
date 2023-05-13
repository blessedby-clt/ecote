N = int(input())
house_list = list(map(int, input().split()))
house_list.sort()
if N % 2 == 0:
    print(house_list[N//2 -1])
else:
    print(house_list[N//2])