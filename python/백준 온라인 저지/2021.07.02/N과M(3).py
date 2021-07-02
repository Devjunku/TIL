import sys
# sys.setrecursionlimit(20000)


input = sys.stdin.readline

N, M = map(int, input().split())

ans = []
def permutation(n):

    if n == M:
        for a in ans:
            print(a, end = ' ')
        print()
        return
    
    for i in range(1, N+1):
        ans.append(i)
        permutation(n+1)
        ans.pop()

permutation(0)



