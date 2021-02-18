from pandas import DataFrame
import sys


sys.stdin = open('input.txt')

def cntword(N_list, N, K):
    cnt = 0
    for i in range(N):
        r_v = 0
        for j in range(N):
            if N_list[i][j]:
                r_v += N_list[i][j]
                if r_v == K and j < N - 1 and N_list[i][j + 1] == 0:
                    cnt += 1
                    r_v = 0
                elif r_v == K and j == N - 1 and N_list[i][j - K] != 1:
                    cnt += 1
                    r_v = 0
            else:
                r_v = 0
    return cnt


def t_mat(N_list):
    for i in range(len(N_list)-1):
        for j in range(i+1, len(N_list)):
            N_list[i][j], N_list[j][i] = N_list[j][i], N_list[i][j]
    return N_list


T = int(input())

for t in range(1, 11):
    N, K = map(int, input().split())
    N_list = []
    for _ in range(N):
        N_list.append(list(map(int, input().split())))

    cnt = 0
    for _ in range(2):
        cnt += cntword(N_list, N, K)
        N_list = t_mat(N_list)

    print('#{} {}'.format(t, cnt))



