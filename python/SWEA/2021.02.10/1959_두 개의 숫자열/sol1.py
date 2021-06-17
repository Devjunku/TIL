import sys

sys.stdin = open('input.txt')

T = int(input())

def multif(large, small):
    multires = []
    for i in range(len(large)-len(small)+1):
        total = 0
        for j in range(len(small)):
             total += (small[j] * large[j+i])
        multires.append(total)

    first = multires[0]
    for i in range(1, len(multires)):
        if first < multires[i]:
            first = multires[i]

    return first


for t in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    if len(N_list) > len(M_list):
        res = multif(N_list, M_list)
    else:
        res = multif(M_list, N_list)

    print('#{} {}'.format(t, res))
