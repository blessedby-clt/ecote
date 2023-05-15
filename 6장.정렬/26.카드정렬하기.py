N = int(input())
card_list = []
for _ in range(N):
    card_list.append(int(input()))

card_list.sort()
cum_count = 0
for idx in range(1, len(card_list)):
    if idx == 1:
        cum_count += card_list[idx] + card_list[idx-1]
    else:
        cum_count += cum_count + card_list[idx]

print(cum_count)