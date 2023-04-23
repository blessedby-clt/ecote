# 정확성 테스트는 통과했으나, 효율성 테스트는 미통과
# (우선순위) 큐에 대한 걸 알아야 하는데 당장 공부를 하지는 못할 것 같아 아래 내용으로 제출

def solution(food_times, k):
    answer = 0
    # 네트워크 중단 되기 전에 음식 다 먹을때
    if k >= sum(food_times):
        return -1
    else:
        # 음식이 충분해서 갖고 있는 음식 순서대로 정렬되는 경우
        if min(food_times)*len(food_times) >= k:
            if (k+1) % len(food_times) == 0:
                return len(food_times)
            else:
                return (k+1) % len(food_times)
        else:
            while k > -1:
                for idx in range(len(food_times)):
                    if food_times[idx] > 0:
                        food_times[idx] -= 1
                        k -= 1
                        answer = idx

                    if k == -1:
                        break
            return answer + 1