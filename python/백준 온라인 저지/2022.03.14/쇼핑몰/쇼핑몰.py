from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
client = deque([list(map(int, input().split())) for _ in range(n)])
visited = [False for _ in range(n)]

goto_outdoor = []

for i in range(k):
    visited[i] = True
    client_ele = client.popleft()
    heappush(goto_outdoor, (client_ele[1], i, client_ele[0]))