# 문제를 못풀어서 해답을 보고 풀었다.
# 공포도 낮은 순으로 정렬해서, 공포도만큼 모험가 배정.
# 공포도 1인 유저는 1명씩, 공포도 2인 유저는 2명씩 묶는 게 최대로 만들 수 있는 방법.

def get_adventurer_group_number():
    number_of_adventurer = int(input())
    fear_score_list = list(map(int, input().split()))
    if number_of_adventurer == len(fear_score_list):
        fear_score_list.sort()
        print(number_of_adventurer)
        print(fear_score_list)
        result = 0
        temp_list = []

        for element in fear_score_list:
            temp_list.append(element)
            if len(temp_list) == element:
                result += 1
                temp_list = []
        return result


if __name__ == '__main__':
    print(get_adventurer_group_number())

