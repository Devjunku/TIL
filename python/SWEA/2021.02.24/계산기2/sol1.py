import sys

sys.stdin = open('input.txt')

token = {
    '*': 2,
    '+': 1
}

for t in range(1, 11):
    N = int(input())
    calcul = input()

    stack = []
    res = []

    for c in calcul:
        if c.isdecimal():
            res.append(c)
        else:
            if len(stack) == 0:
                stack.append(c)
            else:
                while len(stack) != 0 and token[stack[-1]] > token[c]:
                    res.append(stack.pop())
                stack.append(c)


    for s in stack[::-1]:
        res.append(s)
    print(res)
    op_res = []

    for r in res:
        if r.isdecimal():
            op_res.append(int(r))
        elif r == '*':
            v = op_res.pop()
            w = op_res.pop()
            op_res.append(int(w) * int(v))
        elif r == '+':
            v = op_res.pop()
            w = op_res.pop()
            op_res.append(int(w) + int(v))

    print(op_res)


