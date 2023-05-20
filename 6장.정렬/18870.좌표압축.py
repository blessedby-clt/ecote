# 5
# 2 4 -10 4 -9
# 2 3 0 3 1


N = int(input())
number_list = list(map(int, input().split()))
number_unique_list = sorted(list(set(number_list)))
number_dict = {}
new_index_list = []
for i in range(len(number_unique_list)):
    number_dict[number_unique_list[i]] = i

for number in number_list:
    new_index_list.append(number_dict[number])
print(' '.join(map(str, new_index_list)))