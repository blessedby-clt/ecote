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