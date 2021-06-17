import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):
    A = input()
    B = input()
    cnt = 0
    for i in range(len(B)-len(A)+1):
        if B[i:len(A)+i] == A:
            cnt += 1

    print('#{} {}'.format(t, cnt))