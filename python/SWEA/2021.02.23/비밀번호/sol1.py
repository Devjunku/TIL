import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    N, Password = map(str, input().split())

    Pass_list = list(Password)

    stack = []
    for num in Pass_list:
        if len(stack) != 0 and stack[-1] != num:
            stack.append(num)
        elif len(stack) == 0:
            stack.append(num)
        elif len(stack) != 0 and stack[-1] == num:
            stack.pop()

    print('#{} {}'.format(t, ''.join(stack)))
