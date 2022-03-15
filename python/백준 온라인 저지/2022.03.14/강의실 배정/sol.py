import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
lecture = []
for _ in range(n):
    s, e = map(int, input().split())
    lecture.append((s, e))

lecture.sort(key=lambda x: x[0])

hq = []
heappush(hq, lecture[0][1])

for i in range(1, n):
    if hq[0] <= lecture[i][0]:
        heappop(hq)
        heappush(hq, lecture[i][1])
    else:
        heappush(hq, lecture[i][1])
    
print(len(hq))