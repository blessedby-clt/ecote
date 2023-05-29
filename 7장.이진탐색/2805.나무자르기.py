# 링크 : https://www.acmicpc.net/problem/2805
# 시간초과가 일어나서, 인터넷에서 모범답안 검색.
n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

start = 1
end = max(tree_list)

result = 0
while start <= end:
    mid = (start + end) // 2
    # 가져가려고 하는 나무의 양 초기화
    result = 0
    for tree in tree_list:
        # tree - mid 가 0보다 클 때만 가져가야 할 나무 양에 더함.
        if tree - mid > 0:
            result += (tree - mid)
        if result > m:
            break
    if result >= m:
        start = mid + 1

    else:
        end = mid - 1


## 왜 아래 코드로 짜면 시간초과가 나는지 잘 모르겠습니다 ㅠㅠ..
while result != m:
    mid = (start + end) // 2
    result = 0
    for tree in tree_list:
        if tree - mid > 0:
            result += (tree - mid)
        if result > m:
            break
    if result > m:
        start = mid + 1
        # print("result > m")
        # print(result)
        # print("start : ", start)
        # print("end : ", end)
    elif result < m:
        end = mid - 1
        # print("result < m")
        # print(result)
        # print("start : ", start)
        # print("end : ", end)
    else:
        break

print(mid)