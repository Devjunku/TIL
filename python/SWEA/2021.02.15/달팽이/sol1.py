import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    N = int(input())

    arr = [[0 for _ in range(N)] for _ in range(N)]

    i = 1
    r = -1
    c = 0
    direction = 1

    while True:
        for _ in range(N):
            r += direction
            arr[c][r] = i
            i += 1
        N -= 1

        if N < 1:
            break

        for _ in range(N):
            c += direction
            arr[c][r] = i
            i += 1

        direction = -direction

    print('#{}'.format(t))
    for i in range(len(arr)):
        print(*arr[i])








