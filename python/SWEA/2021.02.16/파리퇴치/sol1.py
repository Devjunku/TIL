import sys

sys.stdin = open('input.txt')

T = int(input())

def max_func(x):
    dat = x[0]
    for i in range(1, len(x)):
        if dat < x[i]:
            dat = x[i]
    return dat


for t in range(1, T+1):

    N, M = map(int, input().split())

    N_list = []

    for n in range(N):
        N_list.append(list(map(int, input().split())))

    total = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            my_sum = 0
            for r in range(M):
                for c in range(M):
                    my_sum += N_list[r + i][c + j]

            total.append(my_sum)

    print('#{} {}'.format(t, max_func(total)))






