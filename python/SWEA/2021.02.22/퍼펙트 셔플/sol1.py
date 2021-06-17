import sys

sys.stdin = open('퍼펙트 셔플/sample_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(str, input().split()))
    n = N//2 + N%2
    u_half = data[:n]
    l_half = data[n:N]
    res = []
    if N % 2 == 0:
        for i in range(n):
            res.append(u_half[i])
            res.append(l_half[i])
    else:
        for i in range(n):
            res.append(u_half[i])
            if i == n-1:
                break
            res.append(l_half[i])

    res = ' '.join(res)
    print('#{} {}'.format(t, res))

    