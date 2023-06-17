# 링크 : https://www.acmicpc.net/problem/9372

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def make_edge_count():
    n, p = map(int, input().split())
    parent = [0]*(n+1)
    result = 0

    for i in range(1, n+1):
        parent[i] = i
    for j in range(p):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1

    print(result)


t = int(input())
for i in range(t):
    make_edge_count()