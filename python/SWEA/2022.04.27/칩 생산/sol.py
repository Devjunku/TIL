import sys
sys.stdin = open("sample_sample_input.txt")

def calval(col):
    answer = 0
    mask = 1
    for row in range(H):
        if graph[row][col] == 2:
            answer += mask
        mask <<=1
    return answer
             
def solve(idx, cnt):
     
    if idx == (H-1)*(W-1):
        return cnt
     
    hh = idx%(H-1)
    ww = idx//(H-1)
     
    if hh==0 and ww>1:
        val = calval(ww-1)
        if dp[ww-1][val] != -1:
            return cnt + dp[ww-1][val]
     
    ret1 = 0
    if graph[hh][ww]==graph[hh+1][ww]==graph[hh][ww+1]==graph[hh+1][ww+1]==0:
        graph[hh][ww],graph[hh+1][ww],graph[hh][ww+1],graph[hh+1][ww+1]=2, 1, 1, 1
        ret1 = solve(idx+1, cnt+1)
        graph[hh][ww],graph[hh+1][ww],graph[hh][ww+1],graph[hh+1][ww+1]=0, 0, 0, 0
    ret2 = solve(idx+1, cnt)
     
    ret = max(ret1, ret2)
     
    if hh==0 and ww>1:
        dp[ww-1][val] = ret-cnt
         
    return ret
         
 
T = int(input())
for tc in range(1, T+1):
 
    H, W = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    dp = [[-1]*(2**H+1) for _ in range(W)]
     
    answer = solve(0, 0)
 
    print(f"#{tc} {answer}")