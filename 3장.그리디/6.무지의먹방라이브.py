# 정확성 테스트는 통과했으나, 효율성 테스트는 미통과
# (우선순위) 큐에 대한 걸 알아야 하는데 당장 공부를 하지는 못할 것 같아 아래 내용으로 제출

def solution(food_times, k):
    answer = 0
    # 네트워크 중단 되기 전에 음식 다 먹을때
    # 음식을 다 먹었으면 -1로 리턴.
    if k >= sum(food_times):
        return -1
    else:
        # 네트워크가 끊기는 시점까지 음식이 충분한 경우
        # 이 경우는 현재 보유하고 있는 음식 종류를 다 사용할 수 있고 순서대로 1, 2, 3, 4.. 이렇게 세므로
        # 네트워크 중단시점에 어떤 음식을 먹을지를 나머지만 써서 구할 수 있음.
        if min(food_times)*len(food_times) >= k:
            if (k+1) % len(food_times) == 0:
                return len(food_times)
            else:
                return (k+1) % len(food_times)
        else:
            # 음식이 중간에 모자라는 경우
            # 시간을 하나씩 차감 -> 네트워크 중단 시점에 먹고 있는 음식을 리턴.
            while k > -1:
                for idx in range(len(food_times)):
                    if food_times[idx] > 0:
                        food_times[idx] -= 1
                        k -= 1
                        answer = idx
                        print(k, ":", answer)

                    if k == -1:
                        break
            # 인덱스가 하나씩 밀렸으므로 +1을 더해 맞춰줌.
            return answer + 1

print(solution([3, 1, 2], 5))