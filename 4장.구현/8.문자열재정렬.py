def sort_character(characters):
    string_list = []
    num_list = []
    for char in characters:
        if char.isnumeric():
            num_list.append(char)
        else:
            string_list.append(char)
    # 문자 부분은 그냥 정렬해서 합침.
    string_list.sort()
    result_str = ''.join(string_list)
    # 숫자 부분은 자기들끼리 합을 구함.
    result_num = str(sum(int(element) for element in num_list))
    return result_str + result_num



print(sort_character('K1KA5CB7'))
print(sort_character('AJKDLSI412K4JSJ9D'))
