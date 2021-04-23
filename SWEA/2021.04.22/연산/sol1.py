import sys
sys.stdin = open('sample_input.txt')

from collections import deque

operator = [1, -1, 2, -10]

def bfs(N, M):
    now = deque()
    cnt = 0
    now.append((N, cnt))
    visited = {}
    while now:
        n, c = now.popleft()

        if visited.get(n, 0):
            continue

        if n == M:
            return c
        
        c += 1

        for oper in operator:
            if oper == 2:
                num = n * 2
                if 1 <= num <= 1000000:
                    now.append((num, c))
            else:
                num = n + oper
                if 1 <= num <= 1000000:
                    now.append((num, c))


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{t} {bfs(N, M)}')


    