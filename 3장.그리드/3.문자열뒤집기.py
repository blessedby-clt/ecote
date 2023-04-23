number_str = '0001100'
temp_list = []
number_list = []
comparision_number = '0'

for element in number_str:
    if element != comparision_number:
        temp_list = []
        if comparision_number == '0':
            comparision_number = '1'

        else:
            comparision_number = '0'
    temp_list.append(element)
