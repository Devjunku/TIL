import sys
input = sys.stdin.readline

n = int(input())
result = -2 ** 31 - 1

def calc(num, op):
    while op:
        oper = op.pop(0)
        n1, n2 = num.pop(0), num.pop(0)
        if oper == "+":
            num.insert(0, n1 + n2)
        elif oper == "-":
            num.insert(0, n1 - n2)
        elif oper == "*":
            num.insert(0, n1 * n2)
    return num[0]


def solve(cnt, num, op):
    global result
    if cnt == n // 2 or len(num) == 1:
        result = max(result, calc(num, op))
        return
    
    solve(cnt + 1, num[:], op[:])

    try:
        n1, n2 = num.pop(cnt), num.pop(cnt)
        oper = op.pop(cnt)
        if oper == "+":
            num.insert(cnt, n1 + n2)
        elif oper == "-":
            num.insert(cnt, n1 - n2)
        elif oper == "*":
            num.insert(cnt, n1 * n2)
        
        solve(cnt + 1, num[:], op[:])
    except:
        0

expr = input()
num, op = [], []
for i in range(n):
    if i % 2 == 0:
        num.append(int(expr[i]))
    else:
        op.append(expr[i])

solve(0, num, op)
print(result)