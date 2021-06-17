import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1, 4):
    string = input().replace('()', 'l')
    stack = 0
    cnt = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack += 1
            cnt += 1
            # print(i, '(' ,'stack:', stack, 'cnt:', cnt)
        elif string[i] == 'l':
            cnt += stack
            # print(i, 'l' ,'stack:', stack, 'cnt:', cnt)
        else:
            stack -= 1
            # print(i, ')' ,'stack:', stack, 'cnt:', cnt)
    print('#{} {}'.format(t, cnt))
