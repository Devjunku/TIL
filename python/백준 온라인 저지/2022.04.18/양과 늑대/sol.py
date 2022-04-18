n = 0
wolf_sheep = []
r = [-1] * 17
l = [-1] * 17
visited = [False] * (1 << 17)
ans = 0

def cal_max_sheep(state):
    global ans

    if visited[state]: return

    visited[state] = True
    wolf, num = 0, 0
    
    for i in range(n):
        if state & (1 << i):
            wolf += wolf_sheep[i]
            num += 1
    
    if (2 * wolf) >= num: return
    
    ans = max(ans, num - wolf)

    for i in range(n):
        if ~ state & (1 << i): continue

        if r[i] != -1: cal_max_sheep(state | (1 << r[i]))
        if l[i] != -1: cal_max_sheep(state | (1 << l[i]))


def solution(info, edges):
    global wolf_sheep, n

    n = len(info)
    wolf_sheep = info

    for p, c in edges:
        if r[p] == -1: r[p] = c
        else: l[p] = c

    cal_max_sheep(1)
    return ans
    

if __name__ == "__main__":
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
    print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))