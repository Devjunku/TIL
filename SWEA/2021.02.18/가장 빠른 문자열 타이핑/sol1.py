import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    A, B = map(str, input().split())

    N = len(A)
    M = len(B)
    cnt = 0
    i = 0
    while i < N - M + 1:
        if A[i:i+M] == B:
            cnt += 1
            i += M
        else:
            i += 1

    print('#{} {}'.format(t, N+cnt*(1-M)))
