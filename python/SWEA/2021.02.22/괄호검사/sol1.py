import sys

sys.stdin = open('sample_input.txt')


def solution(string):
    stack = []
    for s in range(len(string)):
        if string[s] == '(' or string[s] == '{':
            stack.append(string[s])
        elif string[s] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif string[s] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0
    if len(stack) != 0:
        return 0
    else:
        return 1

T = int(input())

for t in range(1, T+1):
    try:
        string = input()
        print('#{} {}'.format(t, solution(string)))
    except:
        print('#{} {}'.format(t, 0))





