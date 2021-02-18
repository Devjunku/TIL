import sys

sys.stdin = open('input.txt')

T  =int(input())
for t in range(1, T+1):
    N = list(map(int, list(input())))
    # print(t,N)

    max_num = N[0]
    for i in range(1, len(N)):
        if max_num < N[i]:
            max_num = N[i]
    cnt = [0] * (max_num+1)

    for i in range(len(N)):
        cnt[N[i]] += 1
    # print(cnt)

    if len(cnt) == 1:
        print('#{0} {1}'.format(t, 1))
    elif cnt[len(cnt)-1] == 6:
        print('#{0} {1}'.format(t, 1))
    else:
        baby_jin = 0
        for i in range(len(cnt)):
            if cnt[i] >= 3:
                baby_jin += 1
                cnt[i] -= 3
            if i < max_num - 1 and cnt[i] == 2 and cnt[i + 1] == 2 and cnt[i + 2] == 2:
                baby_jin += 2
                break
            elif i < max_num - 1 and cnt[i] and cnt[i + 1] and cnt[i + 2]:
                baby_jin += 1
                cnt[i] -= 1
                cnt[i + 1] -= 1
                cnt[i + 2] -= 1
        if baby_jin == 2:
            print('#{0} {1}'.format(t, 1))
        else:
            print('#{0} {1}'.format(t, 0))










