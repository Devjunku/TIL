import sys

sys.stdin = open('sample_input.txt')


def card_number(string):
    redu_s = [0] * 13
    redu_d = [0] * 13
    redu_h = [0] * 13
    redu_c = [0] * 13
    i = 0
    while i < len(string):
        if string[i] == 'S':
            redu_s[int(string[i+1:i+3])-1] += 1
            i += 3
        elif string[i] == 'D':
            redu_d[int(string[i+1:i+3])-1] += 1
            i += 3
        elif string[i] == 'H':
            redu_h[int(string[i+1:i+3])-1] += 1
            i += 3
        elif string[i] == 'C':
            redu_c[int(string[i+1:i+3])-1] += 1
            i += 3

    for i in range(13):
        if redu_s[i] > 1 or redu_d[i] > 1 or redu_h[i] > 1 or redu_c[i] > 1:
            return ['ERROR']

    return [13-sum(redu_s),
            13-sum(redu_d),
            13-sum(redu_h),
            13-sum(redu_c)]

T = int(input())

for t in range(1, T+1):
    string = input()
    res = ' '.join(map(str, card_number(string)))
    print('#{} {}'.format(t, res))

