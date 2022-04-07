from itertools import combinations
import sys
input = sys.stdin.readline

def distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

n, m = map(int, input().split())
chk = []
house = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chk.append((i, j))

comb = combinations(chk, m)
answer = int(1e9)

for com in comb:
    res = 0
    for h in house:
        res += min([distance(h[0], h[1], c[0], c[1]) for c in com])
        if answer < res:
            break
    
    answer = min(answer, res)
    
print(answer)