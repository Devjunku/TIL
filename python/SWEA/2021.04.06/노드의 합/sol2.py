import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())

    edge = [0] * (N+1)

    for _ in range(M):
        node, value = map(int, input().split())
        edge[node] = value

    if N % 2:
        i = N
        while i >= L:
            edge[i//2] = edge[i] + edge[i-1]
            i -= 2
    else:
        i = N
        edge[i//2] = edge[i]
        i -= 1
        while i > 0:
            edge[i//2] = edge[i] + edge[i-1]
            i -= 2

    print(f'#{t} {edge[L]}')




