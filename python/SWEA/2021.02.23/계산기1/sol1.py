import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    calculation = list(input())
    i = 0
    nums = ''
    opes = ''
    while i < N-2:
        if calculation[i].isdigit():
            nums += calculation[i]
        elif not calculation[i].isdigit():
            opes += calculation[i]
        i += 1
    postfix = nums + opes + calculation[N-1] + '+'

    stack = []
    i = 0
    while i < len(postfix):
        if postfix[i].isdigit():
            stack.append(int(postfix[i]))
        elif postfix[i] == '+':
            num = stack[-1] + stack[-2]
            stack.pop()
            stack.pop()
            stack.append(num)
        i += 1
    print('#{} {}'.format(t, *stack))



