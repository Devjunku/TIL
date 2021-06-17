import sys

sys.stdin = open('sample_input.txt')

def t_mat(N_list):
    for i in range(len(N_list)-1):
        for j in range(i+1, len(N_list)):
            N_list[i][j], N_list[j][i] = N_list[j][i], N_list[i][j]
    return N_list

T = int(input())

for t in range(1, T+1):
    N, M  = map(int, input().split())
    arr = []
    for n in range(N):
        arr.append(list(input()))

    for _ in range(2):
        for i in range(len(arr)):
            for j in range(len(arr[i])-M+1):
                pali = ''.join(arr[i][j:M+j])
                if pali == pali[::-1]:
                    print('#{} {}'.format(t, pali))
                    break
        arr = t_mat(arr)


