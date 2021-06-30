import sys
from itertools import permutations

def operating(num1, n, e):

    if e == '+':
        res = num1 + n
    elif e == '-':
        res = num1 - n
    elif e == '*':
        res = num1 * n
    else:
        if num1 < 0:
            res = -(abs(num1) // n)
        else:
            res = num1 // n
    return res

dic_operator = {
    0: '+',
    1: '-',
    2: '*',
    3: '//'
}

N = int(input())

nums = list(map(int, input().split()))

num1 = nums[0]
num2 = nums[1:]

operator = list(map(int, input().split()))
permuta_input = []
for i in range(4):
    if operator[i]:
        for _ in range(operator[i]):
            permuta_input.append(dic_operator[i])

start_operate = list(set(permutations(permuta_input, N-1)))
max_v = -sys.maxsize
min_v = sys.maxsize

for s_e in start_operate:
    num1 = nums[0]
    for n, e in zip(num2, s_e):
        res = operating(num1, n, e)
        num1 = res
    
    if max_v < res:
        max_v = res
    
    if min_v > res:
        min_v = res

print(max_v)
print(min_v)