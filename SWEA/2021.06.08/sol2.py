import sys

sys.stdin = open('sample_sample_input.txt')

def dfs(y,x,c):

    if x == W:
        return c

    if y == H-1:
        ans = dfs(0,x+1,c)
        return ans
        
    elif y == 0:
        ptr = 0

        for i_ in range(H):
            if board[i_][x] != 0:
                ptr = ptr | (1 << i_)
                
        if memo[ptr][x] < c:
            memo[ptr][x] = c
        else:
            return 0
  
    cnt = 0
    ans = 0
    for [ny,nx] in [[y,x+1],[y+1,x],[y+1,x+1],[y,x]]:
        if 0<=ny<H and 0<=nx<W and board[ny][nx] == 0:
            cnt += 1
    if cnt == 4:
        for [ny,nx] in [[y,x+1],[y+1,x],[y+1,x+1],[y,x]]:
            board[ny][nx] = 2
        poss1 = dfs(y+1,x,c+1)
        ans = max(ans,poss1)
        for [ny,nx] in [[y,x+1],[y+1,x],[y+1,x+1],[y,x]]:
            board[ny][nx] = 0
    poss2 = dfs(y+1,x,c)
    ans = max(ans,poss2)
    return ans
  
  
  
T = int(input())
  
for tc in range(1,T+1):
    H,W = map(int,input().split())
    memo = [[-1]*W for _ in range(2 ** H)]
    board = [list(map(int,input().split())) for _ in range(H)]
    ans = dfs(0,0,0)
    print('#%d %d'%(tc,ans))