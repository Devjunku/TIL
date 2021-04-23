import sys

sys.stdin = open('sample_input.txt')


'''
크루스칼 알고리즘으로 푸니까 안댐ㅎ
'''


def who_parent(x):
    if parent[x] != x:
        return who_parent(parent[x])
    else:
        return parent[x]


def merge_parent(p1, p2):
    res1 = who_parent(p1)
    res2 = who_parent(p2)

    if res1 > res2:
        parent[res1] = res2
    else:
        parent[res2] = res1
    

def is_equal(n1, n2):
    return who_parent(n1) == who_parent(n2)


T = int(input())

for t in range(1, T+1):
    N, E = map(int, input().split())

    parent = [i for i in range(N+1)]

    edge = []
    for _ in range(E):
        edge.append(list(map(int, input().split())))
    
    edge.sort(key=lambda x: -x[2])

    total = 0
    while edge:
        node1, node2, v = edge.pop()

        if not is_equal(node1, node2):
            merge_parent(node1, node2)
            total += v

    print(v)