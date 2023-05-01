def possible(answer):
    for x, y, stuff in answer:
        # 설치된 것이 기둥
        if stuff == 0:
            # 바닥 위 / 보의 한쪽 끝 부분 위 / 다른 기둥 위라면 정상
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            # 양쪽 끝부분이 보에 연결 또는 한쪽 끝부분이 기둥 위에 있다면 정상
            if ([x-1, y, 1] in answer and [x+1, y, 1] in answer) or [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 삭제인 경우는
        if operate == 0:
            # 일단 삭제를 해 본 후에
            answer.remove([x, y, stuff])
            # 삭제가 불가능하면 다시 복원
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1],
             [4, 2, 1, 1], [3, 2, 1, 1]]))