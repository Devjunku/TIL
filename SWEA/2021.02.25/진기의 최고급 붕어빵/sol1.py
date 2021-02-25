import sys

sys.stdin = open('input.txt')

def solution(per_N, M, K):
    stack = 0
    tm = -1

    per_tm = [0]*(max(per_N) + 1)

    for i in per_N:
        per_tm[i] += 1
    # print(sum(per_tm))
    while tm < len(per_tm)-1:
        tm += 1
        if tm != 0 and tm % M == 0:
            stack += K
            if per_tm[tm] == 0:
                continue
        elif per_tm[tm] > 0 and stack == 0:
            return 'Impossible'
        elif per_tm[tm] > 0 and stack > 0:
            while per_tm[tm] > 0:
                if stack == 0:
                    return 'Impossible'
                per_tm[tm] -= 1
                stack -= 1
    return 'Possible'


T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    per_N = list(map(int, input().split()))
    print('#{} {}'.format(t, solution(per_N, M, K)))


