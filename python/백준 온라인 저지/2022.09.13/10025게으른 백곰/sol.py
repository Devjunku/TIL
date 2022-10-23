"""
4 7
10 15
2 2
5 1

0 5 2 0 0 0 0 4
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pail = [0 for _ in range(1000001)]

for _ in range(n):
    g, x = map(int, input().split())
    pail[x] = g

left = 0
right = int(2*k)
answer = sum(pail[left:right+1])
value = sum(pail[left:right+1])

while True:
    value -= pail[left]
    left += 1; right += 1
    if right >= 1000000: break
    
    value += pail[right]
    answer = max(answer, value)

print(answer)