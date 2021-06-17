import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    N_list = [0] * (N+1)
    # print(N)
    # print(M_list)
    for i in range(len(M_list)):
        N_list[M_list[i]] = 1
    # print(N_list)
    K1 = int(K)
    loca = 0
    cnt = 0

    while True:
        # print('위치:', loca, K1, cnt, N)
        if loca + K1 >= N:
            print('#{} {}'.format(t, cnt))
            break
        if K1 == 0:
            print('#{} {}'.format(t, 0))
            break
        elif N_list[K1 + loca] == 1:
             loca += K1
             cnt += 1
             K1 = int(K)
        else:
             K1 -= 1




