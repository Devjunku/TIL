import sys

sys.stdin = open('input.txt')

def post_oper(string):
    stack = []
    res = ''
    for s in string:
        if s.isdigit():
            res += s
        else:
            if s == '(':
                stack.append(s)
            elif s == '*' or s == '/':
                while stack and (stack[-1] != '*' or stack[-1] != '/'):
                    res += stack.pop()
                stack.append(s)
            elif s == '+' or s == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(s)
            elif s == ')':
                while stack and stack != '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()
        
    return res