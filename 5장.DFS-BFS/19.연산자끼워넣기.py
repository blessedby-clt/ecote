from itertools import permutations
# number_list = [1, 2, 3, 4, 5, 6]
# calc_operator = ["+", "+", "-", "*", "/"]
n = 3
number_list = [3,4,5]
calc_list = list(map(int, "1 0 1 0".split()))
calc_operator = ["+"]*calc_list[0] + ["-"]*calc_list[1] + ["*"]*calc_list[2] + ["/"]*calc_list[3]
calc_comb = list(permutations(calc_operator, n-1))

max_value = -1e9
min_value = 1e9

def calc(idx, answer):
    for i in range(1, len(calc_operator)+1):
        if calc_comb[idx][i-1] == "+":
            answer += number_list[i]
        elif calc_comb[idx][i-1] == "*":
            answer *= number_list[i]
        elif calc_comb[idx][i-1] == "-":
            answer -= number_list[i]
        elif calc_comb[idx][i-1] == "/":
            answer = int(answer / number_list[i])
    return answer
def check_min_max(answer, max_value, min_value):
    if answer > max_value:
        max_value = answer
    if answer < min_value:
        min_value = answer
    return max_value, min_value

for idx in range(len(calc_comb)):
    answer = number_list[0]
    answer = calc(idx, answer)
    max_value, min_value = check_min_max(answer, max_value, min_value)

print(max_value)
print(min_value)