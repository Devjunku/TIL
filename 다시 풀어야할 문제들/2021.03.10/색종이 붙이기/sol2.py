import sys

arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0] * 5
res = sys.maxsize

def back_trak(x, y, cnt):
    if y >= 10:
        res = min(res, cnt)
        return
    if x >= 10:
        back_trak(0, y+1, cnt)
        return
    
    if arr[x][y] == 1:
        for k in range(5):
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue
            flag = 0
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    if arr[i][j] == 1:
                        flag += 1
                        break
                if flag:
                    break
            
            if not flag:
                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        a[i][j] = 0
            
            paper[k] += 1
            back_trak(x+k+1, y, cnt+1)
            paper[k] -= 1

            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    a[i][j] = 1
    
    else:
        back_trak(x+1, y, cnt+1)
