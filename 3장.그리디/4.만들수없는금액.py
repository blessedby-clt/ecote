# 풀고 나니 그리디 문제 풀이가 아닌듯
# 1. 동전으로 만들 수 있는 조합을 구한다.
# 2. 조합을 SET(집합) 형태로 만들어서, 중복 제거 - 집합 A
# 3. 조합의 최소값 ~ 최대값만큼 집합을 만듦. - 집합 B
# 4. 집합 A와 집합 B의 차집합에서 가장 작은 값을 구함.

import itertools

def get_impossible_amount(n, amount_string):
    target_list = [int(i) for i in amount_string.split()]
    if n == len(target_list):
        sum_list = []
        for idx in range(1, len(target_list) + 1):
            a = itertools.combinations(target_list, idx)
            sum_list += [sum(j) for j in a]
        sum_unique_set = set(sum_list)
        sum_all_set = set(range(1, max(sum_list)+1))
        return min(sum_all_set - sum_unique_set)
    else:
        return None

print(get_impossible_amount(5, '3 2 1 1 9'))
print(get_impossible_amount(3, '3 5 7'))



