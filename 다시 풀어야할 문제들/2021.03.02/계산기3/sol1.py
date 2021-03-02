import sys

sys.stdin = open('input.txt')


def post_oper(calcul):
    stack = []
    post_operator = ''
    for s in calcul:
        if s.isdigit():
            post_operator += s
        else:
            if s == '(':
                stack.append(s)
            elif s == '*' or s == '/':
                while stack and (stack[-1] == '*' and stack[-1] == '/'):
                    post_operator += stack.pop()
                stack.append(s)
            elif s == '+' or stack == '-':
                while stack and stack[-1] != '(':
                    post_operator += stack.pop()
                stack.append(s)
            elif s == ')':
                while stack and stack[-1] != '(':
                    post_operator += stack.pop()
                stack.pop()

    while stack:
        post_operator += stack.pop()

    return post_operator


for t in range(1, 11):
    N = int(input())
    post_res = post_oper(input())

    stack = []
    for s in post_res:
        if s.isdigit():
            stack.append(s)
        else:
            if s == '+':
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(w+v)
            elif s == '*':
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(w * v)
            elif s == '/':
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(int(w / v))
            elif s == '-':
                v = int(stack.pop())
                w = int(stack.pop())
                stack.append(int(w - v))
    print('#{} {}'.format(t, *stack))






