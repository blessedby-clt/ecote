def solution(food_times, k):
    answer = 0
    if k >= sum(food_times):
        return -1
    else:
        if min(food_times)*len(food_times) >= k:
            if (k+1) % len(food_times) == 0:
                return len(food_times)
            else :
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