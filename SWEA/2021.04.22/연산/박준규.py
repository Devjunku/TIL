import sys

sys.stdin = open('sample_input.txt')

'''
아래가 처음에 한 풀이인데, 샘플 테스트 케이스는 모두 통과 되었지만
샘플 3개만 맞고 나머지 7개는 런타임 에러가 났다.
왜 그런지 생각하다가
아마도 메모리가 초과되서 그런게 아닌가? 생각이 들었다.ㅠ

문제 접근은 그냥 BFS로 접근했다.
예전에 이러한 문제를 푼 경험이 있었는데,

예전 백준 특강 때 주었던 문제가 생각들었다.

'A->B', 이 문제인데 그 때 이 문제의 풀이는 처음 A 부터 B 까지 가는게 아니라
B에서 A로 역추적하는 방법으로 문제를 풀이했던 것으로 기억한다.

근데 다른 풀이로는 해당 연산을 진행하면서 Queue에 담는 BFS 방식이 있었다.

그래서 그렇게 풀이했으나, 으.......ㅠ
'''

# 실패
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

'''
구글링...한 풀이
'''

from collections import deque

def bfs(v):
    count = 0
    q = deque([[v, count]])
    while q:
        v = q.popleft()
        e = v[0]
        count = v[1]
        if not visited[e]:
            visited[e] = True
            if e == K:
                return count
            count += 1
            if (e * 2) <= 100000:
                q.append([e * 2, count])
            if (e + 1) <= 100000:
                q.append([e + 1, count])
            if (e - 1) >= 0:
                q.append([e - 1, count])
    return count

T = int(input())
for t in range(1, T+1):             
    N, K = map(int, input().split())
    visited = [False] * 100001
    print(f'#{t} {bfs(N)}')


'''
사실 아직까지 무엇이 잘못됐는지 모르겠다.
갈길이 멀구나..
'''