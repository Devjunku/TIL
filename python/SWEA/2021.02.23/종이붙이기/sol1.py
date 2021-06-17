import sys

sys.stdin = open('sample_input.txt')


def solution(n):
    if n == 1:
        return 1

    if n > 1:
        if n % 2 == 0 and memo[n] == -1:
            memo[n] = 2 * solution(n - 1) + 1
            return memo[n]
        elif n % 2 != 0 and memo[n] == -1:
            memo[n] = 2 * solution(n - 1) - 1
            return memo[n]


T = int(input())

for t in range(1, T+1):
    N = int(input())
    n = N//10
    memo = [-1] * 1000

    print('#{} {}'.format(t, solution(n)))