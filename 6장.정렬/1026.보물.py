# 5
# 1 1 1 6 0
# 2 7 8 3 1

n = int(input())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()
array_b.sort(reverse=True)

print(sum([array_a[i]*array_b[i] for i in range(n)]))
