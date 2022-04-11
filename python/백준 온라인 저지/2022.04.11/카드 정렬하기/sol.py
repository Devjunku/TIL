from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
pq = []

for _ in range(n):
    heappush(pq, int(input())) 

answer = 0
while len(pq) > 1:
    temp = heappop(pq) + heappop(pq)
    answer += temp
    if not pq:
        break
    heappush(pq, temp)

print(answer)