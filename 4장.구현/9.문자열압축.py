# 문제 풀이 과정을 보고 풂.
# 풀이과정을 이해한대로 써보면, 완전 구현 방법으로 그냥 하나씩 룰을 구현해보고 제일 적합한 값을 도출하는 프로세스.
s = 'abcabcabcabcdededededede'
answer = len(s)

def write_compressed_result(compress_count, prev, compressed):
    if compress_count > 1:
        compressed += str(compress_count) + prev
    else:
        compressed += prev
    return compressed
# 몇 칸씩 묶을 건지(1 -> 2 -> 3 -> ...)
for step in range(1, int(len(s) / 2) + 1):
    # 압축한 결과값을 compressed로 정의
    compressed = ""
    prev = s[:step]
    # compress_count = 압축계수(abab -> 2ab 이 때 2를 compress count로 정의)
    compress_count = 1
    for j in range(step, len(s), step):
        current = s[j:j+step]
        # 이전값과 현재값이 같다면, 계수를 하나씩 올려준다.
        if prev == current:
            compress_count += 1
        # 이전값과 현재값이 다르다면, 압축 결과값에 써준다.
        # 압축 계수를 1보다 큰 값으로 갖고 있는 경우는 압축계수까지 포함해서 써준다.
        else:
            compressed = write_compressed_result(compress_count, prev, compressed)
            prev = current
            compress_count = 1
    print(f"compress_count : {compress_count}, prev : {prev}, compressed : {compressed}")
    compressed = write_compressed_result(compress_count, prev, compressed)
    print(compressed)
    answer = min(answer, len(compressed))

print(answer)


