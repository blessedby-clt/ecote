map_list = [
    [10, 100, 20, 90],
    [80, 100, 60, 70],
    [70, 20, 30, 40],
    [50, 20, 100, 10]
]
connect_list = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
# 5 10
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
city_index = 1
def renew_connect_list(city_index, r, c):
    if connect_list[r][c] != 0:
        pass
    connect_list[r][c] = city_index
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if nx >= 0 and nx < 4 and ny >= 0 and ny < 4:
            if connect_list[nx][ny] != 0:
                pass
            else:
                if abs(map_list[nx][ny] - map_list[r][c]) >= 10 and abs(map_list[nx][ny] - map_list[r][c]) <= 50:
                    # connect_list[nx][ny] = city_index
                    renew_connect_list(city_index, nx, ny)
                else:
                    connect_list[nx][ny] = -1


# def get_average_pop():
#     for r in range(3):
#         for c in range(3):
#             if connect_list[r][c] > 0:

for r in range(4):
    for c in range(4):
        renew_connect_list(city_index, r, c)
        city_index += 1
print(connect_list)
print(city_index)