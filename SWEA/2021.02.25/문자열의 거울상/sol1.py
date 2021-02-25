import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    dat = list(input())
    for i in range(len(dat)):
        if dat[i] == 'b':
            dat[i] = 'd'
        elif dat[i] == 'd':
            dat[i] = 'b'
        elif dat[i] == 'p':
            dat[i] = 'q'
        elif dat[i] == 'q':
            dat[i] = 'p'

    print('#{} {}'.format(t, ''.join(dat[::-1])))

