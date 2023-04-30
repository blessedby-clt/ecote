from itertools import permutations

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]


def solution(n, weak, dist):
    length = len(weak)
    # 길이를 2배로 늘려서 원형을 일자로 변형
    weak = weak + [element + n for element in weak]
    answer = len(dist) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            print("friends", friends)
            # 투입인원은 1명부터 시작
            count = 1
            # 한 번 이동 후 얼마나 가는지(점검 가능 부분)
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                print("index", index)
                print("count", count)
                print(f"postion : {position}")
                # 취약 지점이 점검 가능 부분을 벗어 나는 경우 새로운 친구를 투입
                if position < weak[index]:
                    count += 1
                    # 더 투입이 불가능한 경우는 종료
                    if count > len(dist):
                        break
                    # 새로 추가된 친구는 이전 친구가 커버 못하는 취약지점부터 시작. 점검 가능 부분을 새롭게 갱신.
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer


print(solution(n, weak, dist))
