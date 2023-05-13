N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
fail_count = [0 for i in range(N+1)]
user_count = [len(stages) for i in range(N+1)]
fail_rate = {i+1:0 for i in range(N)}
final_info = []
cum_fail = 0
for user in stages:
    fail_count[user-1] += 1

for idx in range(len(fail_count)):
    user_count[idx] -= cum_fail
    cum_fail += fail_count[idx]

for stage in range(N):
    fail_rate[stage+1] = fail_count[stage] / user_count[stage]

fall_info = sorted(fail_rate.items(), key = lambda x:(-x[1], x[0]))
for stage in fall_info:
    final_info.append(stage[0])

print(final_info)

## 과거 풀었던 코드
def solution(N, stages):
    cal = 0
    result = {}
    for idx in range(1,N+1) :
        if len(stages) != cal :
            result[idx] = stages.count(idx) / (len(stages) - cal)
            cal += stages.count(idx)
        else :
            result[idx] = 0

    return [i for i, k in sorted(result.items(), key = lambda x : (-x[1], x[0]))]