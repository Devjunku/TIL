from pprint import pprint
from copy import deepcopy
import sys
input = sys.stdin.readline

magic_start = [list(input().strip()) for _ in range(5)]

pprint(magic_start)

loc = []

alpha = {
    "A": [False, 1],
    "B": [False, 2],
    "C": [False, 3],
    "D": [False, 4],
    "E": [False, 5],
    "F": [False, 6],
    "G": [False, 7],
    "H": [False, 8],
    "I": [False, 9],
    "J": [False, 10],
    "K": [False, 11],
    "L": [False, 12],
}

for i in range(5):
    for j in range(9):
        if magic_start[i][j] == 'x':
            loc.append((i, j))
        elif not magic_start[i][j] == '.':
            alpha[magic_start[i][j]][0] = True

not_use = []

for k, v in alpha.items():
    if not v[0]:
        not_use.append(k)

print(not_use)

def is_magic_start(magic_start):
    one = magic_start[0][4] + magic_start[1][3] + magic_start[2][2] + magic_start[3][1]
    two = magic_start[0][4] + magic_start[1][5] + magic_start[2][6] + magic_start[3][7]
    three = magic_start[1][1] + magic_start[1][3] + magic_start[1][5] + magic_start[1][7]
    four = magic_start[3][1] + magic_start[3][3] + magic_start[3][5] + magic_start[3][7]
    five = magic_start[1][1] + magic_start[2][2] + magic_start[3][3] + magic_start[5][5]
    six = magic_start[5][5] + magic_start[4][5] + magic_start[3][6] + magic_start[2][7]

    if one == two and two == three and three == four and four == five and five == six:
        return True

    return False

l = len(loc)

answer = []

def dfs(idx, ms):
    if idx >= l-1:
        if is_magic_start(ms):
            ss = ""
            for m in ms: ss += "".join(m)
            answer.append((ss, ms))
        return
    
    for ll in loc:
        