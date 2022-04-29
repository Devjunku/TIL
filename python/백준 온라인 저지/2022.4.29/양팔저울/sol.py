import sys
input = sys.stdin.readline

def dfs(n_list, n, now, left, right):
    new = abs(left - right)
    if new not in possible:
        possible.add(new)
    
    if now == n:
        return

    if answer[now][new] == 0:

        dfs(n_list, n, now+1, left+n_list[now], right)
        dfs(n_list, n, now+1, left, right+n_list[now])
        dfs(n_list, n, now+1, left, right)
        answer[now][new] = 1


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
possible = set()
answer = [[0]*15001 for i in range(n+1)]

dfs(n_list, n, 0, 0, 0)
for m in m_list:
    if m in possible:
        print("Y", end=" ")
    else:
        print("N", end=" ")

