import sys
from heapq import heappop, heappush
input = sys.stdin.readline

pq = []

n = int(input())
for _ in range(n):
    numbers = list(map(int, input().split()))

    if not pq:
        for number in numbers:
            heappush(pq, number)
    else:
        for number in numbers:
            if pq[0] < number:
                heappush(pq, number)
                heappop(pq)

print(pq[0])