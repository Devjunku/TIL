import sys
from pprint import pprint
input = sys.stdin.readline

n, m = map(int, input().split())

mapping = [[0] * (m+1)]

for _ in range(n):    
    mapping.append([0] + list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        mapping[i][j] += mapping[i][j-1]

for j in range(1, m+1):
    for i in range(1, n+1):
        mapping[i][j] += mapping[i-1][j]
    
pprint(mapping)


t = int(input())
for _ in range(t):
    ux, uy, bx, by = map(int, input().split())
    print(mapping[bx][by] -  mapping[ux-1][by] - mapping[bx][uy-1] + mapping[ux-1][uy-1])