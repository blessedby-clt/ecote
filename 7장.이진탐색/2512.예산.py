# 링크 : https://www.acmicpc.net/problem/2512

n = int(input())
budget_list = list(map(int, input().split()))
# 전체 예산 상한액
sum_budget = int(input())

start = 1
end = sum_budget

while start <= end:
    mid = (start + end) // 2
    result = 0
    for budget in budget_list:
        # 예산이 mid(예산 상한액)보다 크면 예산 상한액까지만 더함.
        if budget > mid:
            result += mid
        # 예산이 mid(예산 상한액)보다 같거나 작으면 예산만큼 지급.
        else:
            result += budget
    # 예산 합이 전체 예산 상한액보다 크면 end를 낮춰줌
    if result > sum_budget:
        end = mid - 1
    # 아니면 start를 높여줌
    else:
        start = mid + 1

# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
# 만일 모든 예산을 다 더해도, 전체 예산 상한액보다 작다면 그냥 현재 리스트에서 제일 큰 값을 보여줌.
if end >= sum_budget:
    print(max(budget_list))
else:
    print(end)