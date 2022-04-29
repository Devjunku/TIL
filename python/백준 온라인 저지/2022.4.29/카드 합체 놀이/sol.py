import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pq = []
for ai in arr:
    heappush(pq, ai)

for _ in range(m):
    n1 = heappop(pq)
    n2 = heappop(pq)
    n3 = n1 + n2

    heappush(pq, n3)
    heappush(pq, n3)

print(sum(pq))


    