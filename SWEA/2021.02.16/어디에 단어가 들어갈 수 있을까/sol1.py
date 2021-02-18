import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    N, K = map(int, input().split())

    N_list = []
    for _ in range(N):
        N_list.append(list(map(int, input().split())))

    cnt = 0
    for i in range(N):
        r_v = 0
        c_v = 0
        for j in range(N):
            if N_list[i][j]:
                r_v += N_list[i][j]
                if r_v == K and j == N - 1 and N_list[i][j - K] != 1:
                    cnt += 1
                    r_v = 0
                elif r_v == K and j < N - 1 :
                    if N_list[i][j + 1] == 1:
                        r_v = 0
                    elif N_list[i][j + 1] == 0:
                        cnt += 1
                        r_v = 0
            else:
                r_v = 0

            if N_list[j][i]:
                c_v += N_list[j][i]
                if c_v == K and j == N - 1 and N_list[j - K][i] != 1:
                    print('열 기준1', j, i)
                    cnt += 1
                    r_v = 0
                elif c_v == K and j < N - 1 :
                    if N_list[j + 1][i] == 1:
                        c_v = 0
                    elif N_list[j + 1][i] == 0:
                        print('열 기준2', j, i)
                        cnt += 1
                        c_v = 0
            else:
                c_v = 0

    print('#{} {}'.format(t, cnt))





