import sys

# from pandas import DataFrame

# from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    N_list = list(map(int, input().split()))

    for _ in range(M):
        N_list.append(N_list.pop(0))

    print('#{} {}'.format(t, N_list[0]))