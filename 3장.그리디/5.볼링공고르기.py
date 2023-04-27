# 볼링공의 무게를 key로 해서,
# 공이 나온 횟수, 내 무게보다 무서운 공의 개수를 value로 받아옴.
# 1 2 2 3 3 조합일 경우,
# 2번 + 4번 공, 2번 공 + 5번 공 조합도 가능하기 때문.
def choice_ball():
    n, m = map(int, input().split())
    ball_list = list(map(int, input().split()))
    ball_list.sort()
    counter_dict = {}
    result = 0
    for idx in range(len(ball_list)):
        if ball_list[idx] not in counter_dict.keys():
            counter_dict[ball_list[idx]] = [0, 0]
        counter_dict[ball_list[idx]][0] += 1
        # 오름차순으로 정렬 후, 내 무게보다 무거운 공의 개수를 카운트.
        counter_dict[ball_list[idx]][1] = len(ball_list) - (idx + 1)
        print(counter_dict)
    for key in range(1, m+1):
        result += counter_dict[key][0]*counter_dict[key][1]

    return result

print(choice_ball())