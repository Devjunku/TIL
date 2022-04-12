n = 0
wolf_sheep = []

l = [-1] * 20
r = [-1] * 20

visited = [0] * ( 1 << 17)
ans = 0

def dfs(state):
    global ans

    if visited[state]: return

    visited[state] = 1
    num, wolf = 0, 0

    for i in range(n):
        if state & (1 << i):
            num += 1
            wolf += wolf_sheep[i]
    
    if (2*wolf) >= num: return

    ans = max(ans, num - wolf)

    for i in range(n):
        if not state & (1 << i):
            continue

        if l[i] != -1:
            dfs(state | (1 << l[i]))
        
        if r[i] != -1:
            dfs(state | (1 << r[i]))
            

def solution(info, edges):
    global wolf_sheep, n

    n = len(info)
    wolf_sheep = info[:]

    for p, c in edges:
        if l[p] != -1:
            r[p] = c
        else:
            l[p] = c

    dfs(1)

    return ans
    


if __name__ == "__main__":
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
    # 5
    print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
    # 5