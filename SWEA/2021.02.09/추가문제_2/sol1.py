import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    answer = ''
    N, Q = map(int, input().split())
    N_list = [0] * N
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L-1, R):
            N_list[i] = q
    for j in range(len(N_list)):
        answer += str(N_list[j]) + ' '
    print('#{} {}'.format(t, answer[0:len(answer)-1]))
