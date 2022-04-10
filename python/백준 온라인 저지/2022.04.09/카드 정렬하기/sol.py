import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input().strip())

pq = []

for _ in range(n):
    heappush(pq, int(input()))

answer = 0
while len(pq) > 1:
    f = heappop(pq)
    s = heappop(pq)
    answer += (f+s)
    if not pq:
        break
    heappush(pq, f+s)

print(answer)