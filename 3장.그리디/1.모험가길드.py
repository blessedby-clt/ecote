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

