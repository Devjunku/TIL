res = 0
def dfs(cnt, k, dungeons, visited):
    global res

    if k <= 0:
        return

    if cnt > res:
        res = cnt

    for i in range(len(dungeons)):
        if i not in visited and k >= dungeons[i][0]:
            visited.append(i)
            dfs(cnt+1, k - dungeons[i][1], dungeons, visited)
            visited.pop()
            
def solution(k, dungeons):
    visited = []
    dfs(0, k, dungeons, visited)
    return res

if __name__ == "__main__":
    print(solution(80, [[80,20],[50,40],[30,10]]))