from sys import stdin
from itertools import combinations
height = []
for _ in range(9):
    height.append(int(stdin.readline().rstrip()))

acc = combinations(height, 7)

for ac in acc:
    if sum(ac) == 100:
        res = sorted(list(ac))
        for re in res:
            print(re)
        break