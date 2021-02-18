import sys

sys.stdin = open('s_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        A.append(Ai)
        B.append(Bi)

    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))

    res = ''
    for i in range(P):
        cnt = 0
        for j in range(N):
            if A[j] <= C[i] <= B[j]:
                cnt += 1
        res += str(cnt) + ' '

    print('#{} {}'.format(t, res[:len(res)-1]))

