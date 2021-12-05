from collections import deque

n, k = map(int,input().split())
node = [-1 for _ in range(100001)]
node[n] = 0
q = deque()
q.append(n)


while q:
    now = q.popleft()
    if now == k:
        print(node[now])
        break

    if 0 < 2*now < 100001 and node[2*now] == -1:
        node[2*now] = node[now]
        q.appendleft(2*now)

    if 0 <= now + 1 < 100001 and node[now+1] == -1:
        node[now+1] = node[now] + 1
        q.append(now+1)
    
    if 0 <= now - 1 < 100001 and node[now-1] == -1:
        node[now-1] = node[now] + 1
        q.append(now-1)
