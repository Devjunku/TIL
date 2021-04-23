'''
크루스칼 알고리즘
가중치의 합을 최소로 만드는 경우 크루스칼 알고리즘을 사용하면 된다.

알고리즘 진행 방향

1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하면서 현재 간선이 사이클을 발생시키는지 확인
 - 1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함 O
 - 2. 사이클이 발생하면 최소 신장 트리에 포함 X
3. 모든 간선에 대해 2번을 반복
'''

import sys

sys.stdin = open('sample_input.txt')


# 부모 찾기
def who_parent(x):
    if parent[x] != x:
        return who_parent(parent[x])
    else:
        return parent[x]


# 부모 합치기
def merge_parent(p1, p2):
    res1 = who_parent(p1)
    res2 = who_parent(p2)

    if res1 > res2:
        parent[res1] = res2
    else:
        parent[res2] = res1

# 사이클이 발생하는지 확인
def is_equal(p1, p2):
    return who_parent(p1) == who_parent(p2)

T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())

    parent = [i for i in range(v+1)]
    edge = [list(map(int, input().split())) for _ in range(e)]
    # 오름차순으로 정렬
    edge.sort(key=lambda x: -x[2])
    total = 0

    # 가중치가 가장 큰 값부터 반영되므로
    # 차례로 추출했을 때, 최소 신장 트리를 구현할 수 있음
    while edge:
        p1, p2, v = edge.pop()

        # 사이클이 발생하지 않는 경우 트리에 포함하는 것
        if not is_equal(p1, p2):
            merge_parent(p1, p2)
            total += v # 해당 가중치는 더해주기

    print(total)