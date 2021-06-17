import sys

sys.stdin = open('input.txt')

from heapq import heappush, heappop

def make_info(x_loc, y_loc, tax_rate):
    graph = []
    for i in range(N):
        for j in range(i+1, N):
            dist = ((x_loc[i]-x_loc[j])**2 + (y_loc[i]-y_loc[j])**2)*tax_rate
            heappush(graph, (dist, i, j))
    
    return graph


def who_parent(x):
    if parent[x] != x:
        parent[x] = who_parent(parent[x])
    return parent[x]


def union_parent(n1, n2):
    p1 = who_parent(n1)
    p2 = who_parent(n2)

    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1
    

def is_equal(n1, n2):
    return who_parent(n1) == who_parent(n2)


T = int(input())

for t in range(1, T+1):
    N = int(input())
    x_loc = list(map(int, input().split()))
    y_loc = list(map(int, input().split()))
    tax_rate = float(input())
    graph = make_info(x_loc, y_loc, tax_rate)
    
    parent = [i for i in range(N+1)]
    res = 0
    cnt = 0

    while graph and cnt != N-1:

        dist, i, j = heappop(graph)

        if not is_equal(i, j):
            res += dist
            cnt += 1
            union_parent(i, j)
    
    res = int(res+0.5)

    print(f'#{t} {res}')