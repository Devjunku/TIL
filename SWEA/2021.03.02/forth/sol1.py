import sys

sys.stdin = open('sample_input.txt')

def solution(case):
    stack = []
    i = 0
    while i < len(case):
        if case[i].isdigit():
            stack.append(case[i])
        elif case[i] == '+':
            if len(stack) > 1:
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(v + w)
            else:
                return 'error'
        elif case[i] == '-':
            if len(stack) > 1:
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(w - v)
            else:
                return 'error'
        elif case[i] == '*':
            if len(stack) > 1:
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(v * w)
            else:
                return 'error'
        elif case[i] == '/':
            if len(stack) > 1:
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(int(w / v))
            else:
                return 'error'
        elif case[i] == '.':
            if len(stack) == 1:
                return stack[-1]
            else:
                return 'error'
        i += 1

T = int(input())
for t in range(1, T+1):
    case = list(map(str, input().split()))
    print('#{} {}'.format(t, solution(case)))







