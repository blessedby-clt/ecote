# 초기값 -1부터 시작.
# 000111000 이런 식이면, 0묶음 = 2개, 1묶음 = 1개. 작은 묶음 개수를 고른다.

def shuffle_binary_string(binary_string:str):
    number_counter = {'0':0, '1':0}
    init_number = '-1'

    for element in binary_string:
        if element != init_number:
            init_number = element
            number_counter[init_number] += 1
    return min(number_counter['0'], number_counter['1'])


if __name__ == '__main__':
    print(shuffle_binary_string('00011001100'))