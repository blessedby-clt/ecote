# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours

n = int(input())
words_list = []
for word in range(n):
    words_list.append(input())

unique_word_list = list(set(words_list))
unique_word_list.sort(key= lambda x:(len(x), x))

for word in unique_word_list:
    print(word)