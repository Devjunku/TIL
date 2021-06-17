import sys


sys.stdin = open('input.txt')

import heapq

def produce_edge():
    global dist
    for i in range(N):
        for j in range(i+1, N):
            d = ((x_loc[i] - x_loc[j])**2 + (y_loc[i] - y_loc[j])**2)*tax_rate
            heapq.heappush(dist, (d, i, j))


def who_parents(x):
    if parent[x] != x:
        parent[x] = who_parents(parent[x])
    return parent[x]


def merge_parent(x, y):
    x = who_parents(x)
    y = who_parents(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def is_equal(x, y):
    return who_parents[x] == who_parents[y]


T = int(input())

for t in range(1, T+1):
    N = int(input())
    x_loc = list(map(int, input().split()))
    y_loc = list(map(int, input().split()))
    tax_rate = float(input())

    parent = [i for i in range(N)]
    dist = []

    produce_edge()
    res = 0
    cnt = 0

    while dist and cnt != N - 1:
        d, i, k = heapq.pop(dist)

        if not is_equal(i, k):
            res += d
            cnt += 1
            merge_parent(i, j)

    res = int(res+0.5)

    print(f'#{t} {res}')