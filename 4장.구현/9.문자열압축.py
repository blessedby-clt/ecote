## 문제 풀이 과정을 보고 풂.

s = 'abcabcabcabcdededededede'
answer = len(s)
for step in range(1, int(len(s) / 2) + 1):
    compressed = ""
    prev = s[:step]
    compress_count = 1
    for j in range(step, len(s), step):
        # print(step)
        current = s[j:j+step]
        # print(compress_count)
        # print("prev : ",prev)
        # print("current :", current)
        if prev == current:
            compress_count += 1
        else:
            if compress_count > 1:
                compressed += str(compress_count) + prev
            else:
                compressed += prev
            prev = current
            compress_count = 1
    if compress_count > 1:
        compressed += str(compress_count) + prev
    else:
        compressed += prev
    answer = min(answer, len(compressed))

print(answer)


