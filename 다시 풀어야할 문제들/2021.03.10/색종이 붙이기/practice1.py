import sys

input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
res = sys.maxsize

def backtracking(x, y, cnt):
    global res

    if y >= 10:
        res = min(res, cnt)
        return
    
    if x >= 10:
        backtracking(0, y+1, cnt)
        return

    if arr[x][y] == 1:
        for num in range(5):
            if paper[num] == 5:
                continue

            if x + num >= 10 or y + num >= 10:
                continue

            flag = 0
            for i in range(x, x+num+1):
                for j in range(y, y+num+1):
                    if arr[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break
            
            if not flag:
                for i in range(x, x+num+1):
                    for j in range(y, y+num+1):
                        arr[i][j] = 0
            
                paper[num] += 1
                backtracking(x+num+1, y, cnt+1)
                paper[num] -= 1

                for i in range(x, x+num+1):
                    for j in range(y, y+num+1):
                        arr[i][j]= 1
    else:
        backtracking(x+1, y, cnt)

backtracking(0, 0, 0)

print(res) if res != sys.maxsize else print(-1)