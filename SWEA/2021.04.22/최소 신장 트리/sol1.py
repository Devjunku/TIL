import sys

sys.stdin = open('sample_input.txt')


def who_parent(x):
    if parent[x] != x:
        parent[x] = who_parent(parent[x])
    return parent[x]


def merge_parent(n1, n2):
    parent1 = who_parent(n1)
    parent2 = who_parent(n2)

    if parent1 > parent2:
        parent[parent1] = parent2
    else:
        parent[parent2] = parent1


def is_equal(n1, n2):
    return who_parent(n1) == who_parent(n2)


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    parent = [v for v in range(V+1)]
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x: -x[2])
    # print(parent)
    total = 0
    print(edge)
    while edge:
        n1, n2, v = edge.pop()
        print(n1, n2)
        print(who_parent(n1), who_parent(n2), v)
        if not is_equal(n1, n2):
            merge_parent(n1, n2)
            print(parent)
            total += v
    
    print(f'#{t} {total}')


    