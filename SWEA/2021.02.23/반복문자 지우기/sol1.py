import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, T+1):

    string = input()
    res = []
    for s in string:
        if len(res) == 0 or res[-1] != s:
            res.append(s)
        elif res[-1] == s:
            res.pop()

    print('#{} {}'.format(t,len(res)))