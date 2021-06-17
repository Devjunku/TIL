def sum_func(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total


import sys

sys.stdin = open('sample_input.txt')

T = int(input())


for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    M = len(A)
    cnt = 0
    for i in range(1 << M):
        partition = []
        for j in range(M):
            if i & (1 << j):
                partition.append(A[j])
        if len(partition) != N:
            continue
        elif len(partition) == N and sum_func(partition) == K:
            cnt += 1

    print('#{} {}'.format(t, cnt))













