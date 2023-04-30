from itertools import combinations
num_of_shop = 2
# city_map = [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]
city_map = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]
# city_map = [[1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0]]
chicken_shop_list = []
house_list = []

# 치킨집, 일반집의 위치 인덱스 추출
for row in range(len(city_map)):
    for element in range(len(city_map[row])):
        if city_map[row][element] == 2:
            chicken_shop_list.append([row, element])
        elif city_map[row][element] == 1:
            house_list.append([row, element])

# 치킨집 조합 만들기
shop_comb = list(combinations(chicken_shop_list, num_of_shop))
print("shop_list", shop_comb)
print("house_list", house_list)
answer = len(city_map) * len(city_map)
for element in shop_comb:
    total_dist = 0
    print(element)
    for house in house_list:
        result = len(city_map) * len(city_map)
        for shop in element:
            print(f"house : {house}, shop:{shop} ")
            dist = abs(shop[0] - house[0]) + abs(shop[1] - house[1])
            if dist < result:
                result = dist
        total_dist += result
    answer = min(total_dist, answer)
print(answer)




