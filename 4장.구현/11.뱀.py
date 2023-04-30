n = 1
m = 1
i = 10
direction = 180
snake = [[1, 1]]
times = 0
# apple = [[3, 4], [2, 5], [5, 3]]
# action = {3:'D', 15:'L', 17:'D'}
# apple = [[1, 2], [1, 3], [1, 4],[1, 5]]
# action = {8 : "D", 10: "D", 11 : "D", 13:"L"}
apple = [[1, 2], [1, 3],[1, 5], [1, 6],[1, 7]]
action = {8 : "D", 10: "D", 11 : "D", 13:"L"}
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
    print(before_n, before_m)
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
    print(snake)
