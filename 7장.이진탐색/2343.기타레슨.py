# 링크 : https://www.acmicpc.net/problem/2343

n, m = map(int, input().split())
lesson_list = list(map(int, input().split()))
start = max(lesson_list)
end = sum(lesson_list)
answer = sum(lesson_list)

while start <= end:
    # 자체 상한선
    mid = (start + end) // 2
    # 블루레이 개수 리스트
    result = []
    # 블루레이 강의시간 초기값
    result_number = 0
    for number in lesson_list:
        # 강의시간 총계 + 블루레이 강의시간 더한 값이 상한선보다 작으면 계속 더해준다
        if result_number + number <= mid:
            result_number += number
        # 그렇지 않으면 블루레이 리스트에 넣어주고, 강의시간을 현재 강의시간으로 초기화시켜준다.
        else:
            result.append(result_number)
            result_number = number
    # 잔여 강의시간을 처리해준다.
    if result_number <= mid:
        result.append(result_number)
    # 만일 목표한 블루레이 개수보다 크면, start를 높여준다. (블루레이에 강의를 더 구겨 담을 수 있단 뜻이므로..)
    if len(result) > m:
        start = mid + 1
    # 아니면 하한선을 낮춰주고, 최소값 갱신이 가능한지 확인하여 처리한다.
    else:
        end = mid - 1
        max_answer = max(result)
        if answer > max_answer:
            answer = max_answer

print(answer)
