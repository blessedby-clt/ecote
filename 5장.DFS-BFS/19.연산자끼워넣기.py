from itertools import product

number_list = [1, 2, 3, 4, 5,6]
calc_operator = ["+", "+", "-", "*", "/"]
print(list(product(number_list, calc_operator)))