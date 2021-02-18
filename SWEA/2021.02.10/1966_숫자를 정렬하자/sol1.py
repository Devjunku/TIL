import sys

sys.stdin = open('input.txt')

T = int(input())

def sorting(x):
    for i in range(len(x)-1, 0, -1):
        for j in range(0, i):
            if x[j] > x[j+1]:
                x[j], x[j + 1] = x[j+1], x[j]
    return x


for t in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    str_N = map(str, sorting(N_list))

    print('#{} {}'.format(t, ' '.join(str_N)))