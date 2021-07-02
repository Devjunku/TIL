import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = []
def permutation(n):

    if n > 1:
        if ans[-1] < ans[-2]:
            return

    if n == M:
        for a in ans:
            print(a, end = ' ')
        print()
    
    for i in range(1, N+1):
        if i in ans:
            continue
        ans.append(i)
        permutation(n+1)
        ans.pop()


permutation(0)



