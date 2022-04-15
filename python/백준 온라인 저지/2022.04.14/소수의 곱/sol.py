from heapq import heappop, heappush
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(map(int, input().split()))

pq = []

for a in arr:
    heappush(pq, a)

for i in range(n):
    num = heappop(pq)
    for j in range(k):
        new_num =  num * arr[j]
        heappush(pq, new_num)
    
        if num % arr[j] == 0:
            break
else:
    print(num)