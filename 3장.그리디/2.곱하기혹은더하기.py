# 왼쪽, 오른쪽 각각 더해보거나, 곱해봐서 큰 값을 취함.
def plus_or_multiply(number_str: str):

    result = int(number_str[0])
    for i in range(1, len(number_str)):
        plus_result = result + int(number_str[i])
        multiply_result = result * int(number_str[i])

        result = max(plus_result, multiply_result)

    return result


if __name__ == '__main__':
    print(plus_or_multiply('567'))


