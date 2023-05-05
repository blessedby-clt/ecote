# 보드 크기
i = int(input())
# 사과 개수
apple_count = int(input())
# 사과 위치 설정
apple = []
for _ in range(apple_count):
    apple.append(list(map(int, input().split())))
n, m = 1, 1
direction = 180
snake = [[n, m]]
times = 0
# 뱀의 행동횟수
action_count = int(input())
action = {}
for _ in range(action_count):
    temp_action = input().split()
    action[int(temp_action[0])] = temp_action[1]


is_game_continue = True
def change_direction(direction, d):
    if d == "D":
        direction += 90
    elif d == "L":
        direction -= 90
    return direction
def set_snake_head(direction, n, m):
    if direction % 360 == 180:
        m += 1
    elif direction % 360 == 90:
        n -= 1
    elif direction % 360 == 0:
        m -= 1
    elif direction % 360 == 270:
        n += 1

    return n, m
def move_snake(snake):
    if len(snake) == 1:
        snake[-1] = [n, m]
    else:
        for index in range(1, len(snake)):
            snake[len(snake) - index] = snake[len(snake) - index - 1]
        snake[0] = [n, m]
    return snake

while n > 0 and m > 0 and n < i + 1 and m < i + 1 and is_game_continue:
    times += 1
    before_n = n
    before_m = m

    n, m = set_snake_head(direction, n, m)
    if [n, m] in apple:
        snake.append([before_n, before_m])
        apple.remove([n, m])
    if [n, m] in snake:
        is_game_continue = False
    snake = move_snake(snake)
    if times in action.keys():
        direction = change_direction(direction, action[times])

print(times)