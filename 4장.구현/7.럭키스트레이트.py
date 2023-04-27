def check_lucky_straight(score):
    score_index = int(len(score)/2)
    left_score = score[:score_index]
    right_score = score[score_index:]
    left_result = 0
    right_result = 0
    for score in left_score:
        left_result += int(score)
    for score in right_score:
        right_result += int(score)
    if left_result == right_result:
        return 'LUCKY'
    else:
        return 'READY'

print(check_lucky_straight('123402'))
print(check_lucky_straight('7755'))
