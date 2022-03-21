from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
pq = []
lecture = []
for _ in range(n):
    idx, s, e = map(int, input().split())
    heappush(lecture, (s, e, idx))

s, e, idx = heappop(lecture)
heappush(pq, e)

while lecture:
    s, e, idx = heappop(lecture)
    if pq[0] <= s:
        heappop(pq)
    heappush(pq, e)

print(len(pq))