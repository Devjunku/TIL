import sys
from heapq import heappop, heappush
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_pq, max_pq = [], []
    visited = [False for _ in range(1000001)]
    for i in range(k):
        mode, number = input().split()
        
        if mode == "I":
            heappush(min_pq, (int(number), i))
            heappush(max_pq, (-int(number), i))
            visited[i] = True
        elif number == "-1":
            while min_pq and not visited[min_pq[0][1]]:
                heappop(min_pq)
            if min_pq:
                visited[min_pq[0][1]] = False
                heappop(min_pq)
        else:
            while max_pq and not visited[max_pq[0][1]]:
                heappop(max_pq)
            if max_pq:
                visited[max_pq[0][1]] = False
                heappop(max_pq)
    
    while min_pq and not visited[min_pq[0][1]]:
        heappop(min_pq)
    while max_pq and not visited[max_pq[0][1]]:
        heappop(max_pq)
    
    if max_pq and min_pq:
        print(f"{-max_pq[0][0]} {min_pq[0][0]}")
    else:
        print("EMPTY")