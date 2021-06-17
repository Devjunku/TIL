import sys

sys.stdin = open('s_input.txt')

T = int(input())

for t in range(1, T+1):
    D, A_v, B_v, F_v = map(int, input().split())
    v = A_v + B_v
    res = (D / v) * F_v
    print('#{} {}'.format(t, res))