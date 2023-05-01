p = "(()())()"

from collections import Counter
def balanced_index(p):
    for idx in range(len(p)):
        counter = Counter(p[:idx+1])
        if counter["("] == counter[")"]:
            return idx+1
def check_proper(p):
    before_value = ''
    after_value = p
    while before_value != after_value:
        before_value = after_value
        after_value = after_value.replace("()", "")
    if len(after_value) > 0:
        return False
    else:
        return True

def solution(p):
    answer = ""
    if p == "":
        return answer

    index = balanced_index(p)
    u = p[:index]
    v = p[index:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        temp_u = ''
        for str in u:
            if str == '(':
                temp_u += ')'
            else:
                temp_u += '('
        answer += temp_u
    return answer


print(solution(p))