map_list = [
    [10, 100, 20, 90],
    [80, 100, 60, 70],
    [70, 20, 30, 40],
    [50, 20, 100, 10]
]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def renew_connect_list(r, c):
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4 and not connect_list[nx][ny]:
            if abs(map_list[nx][ny] - map_list[r][c]) >= 10 and abs(map_list[nx][ny] - map_list[r][c]) <= 50:
                connect_list[nx][ny] = True
                stack.append([nx, ny])
                renew_connect_list(nx, ny)
count = 0
is_continue = True
# while is_continue:
while count < 5:
    stack_list = []
    connect_list = [[False] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            stack = []
            if not connect_list[r][c]:
                connect_list[r][c] = True
                stack.append([r, c])
                renew_connect_list(r, c)

                if len(stack) > 1:
                    avg = sum([map_list[x][y] for x, y in stack]) // len(stack)
                    for x, y in stack:
                        map_list[x][y] = avg
                stack_list.append(stack)
    print(stack_list)
    if len(stack_list) == 16:
        is_continue = False
        break
    count += 1

print(count)