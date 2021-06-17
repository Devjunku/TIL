import sys

sys.stdin = open('input.txt')

T  =int(input())
for t in range(1, T+1):
    N = list(map(int, list(input())))
    print(t,N)

    max_num = N[0]
    for i in range(1, len(N)):
        if max_num < N[i]:
            max_num = N[i]
    cnt = [0] * (max_num+1)

    for i in range(len(N)):
        cnt[N[i]] += 1
    print(cnt)
    baby_jin = 0
    idx = 0
    while idx < len(cnt):
        if cnt[idx] >= 3:
            baby_jin += 1
            cnt[idx] -= 3
            continue

        if idx < max_num - 1:
            if cnt[idx] and cnt[idx+1] and cnt[idx+2]:
                baby_jin += 1
                cnt[idx] -= 1
                cnt[idx+1] -= 1
                cnt[idx+2] -= 1
                continue
        idx += 1

    if baby_jin == 2:
        print('#{0} {1}'.format(t, 1))
    else:
        print('#{0} {1}'.format(t, 0))
