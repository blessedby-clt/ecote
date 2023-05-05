from itertools import combinations
length_of_map, num_of_shop = map(int,input().split())
city_map = []
for _ in range(length_of_map):
    city_map.append(list(map(int, input().split())))
chicken_shop_list = []
house_list = []

# 치킨집, 일반집의 위치 인덱스 추출
for row in range(length_of_map):
    for element in range(length_of_map):
        if city_map[row][element] == 2:
            chicken_shop_list.append([row, element])
        elif city_map[row][element] == 1:
            house_list.append([row, element])

# 치킨집 조합 만들기
shop_comb = list(combinations(chicken_shop_list, num_of_shop))
answer = (len(city_map)*2) * (len(city_map)*2)
for element in shop_comb:
    total_dist = 0
    for house in house_list:
        result = (len(city_map)*2) * (len(city_map)*2)
        for shop in element:
            # print(f"house : {house}, shop:{shop} ")
            dist = abs(shop[0] - house[0]) + abs(shop[1] - house[1])
            result = min(dist, result)
        total_dist += result
    answer = min(total_dist, answer)

print(answer)