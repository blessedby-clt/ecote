def choice_ball(ball_list):
    ball_list.sort()
    counter_dict = {}
    result = 0
    for idx in range(len(ball_list)):
        if ball_list[idx] not in counter_dict.keys():
            # 등장횟수, 선택가능한 가지수를 리스트로 저장.
            counter_dict[ball_list[idx]] = [0, 0]
        counter_dict[ball_list[idx]][0] += 1
        # 오름차순으로 정렬 후, 내 무게보다 무거운 공의 개수를 카운트.
        counter_dict[ball_list[idx]][1] = len(ball_list) - (idx + 1)
    for key in range(1, 3+1):
        result += counter_dict[key][0]*counter_dict[key][1]
    return result

print(choice_ball([1, 3, 2, 3, 2]))