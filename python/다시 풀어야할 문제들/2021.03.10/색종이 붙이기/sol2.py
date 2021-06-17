import sys

sys.stdin = open('')

arr = [list(map(int, input().split())) for _ in range(10)]
paper_cnt = [0] * 5
ans = sys.maxsize

def back_track(x, y, cnt):
    global paper_cnt, arr
    if y >= 10:
        ans = min(cnt, ans)
        return

    if x >= 10:
        back_track(0, y+1, cnt)
        return
    
    if arr[x][y] == 1:
        for k in range(5):
            if paper_cnt[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    if arr[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        arr[i][j] = 0:
            
                paper_cnt[k] += 1
                back_track(x+k+1, y, cnt+1)
                paper_cnt[k] -= 1

                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        a[i][j] = 1
    else:
        back_track(x+1, y, cnt)

back_track(0, 0, 0)
print(and) if ans != sys.maxsize else print(-1)




    