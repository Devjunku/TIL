l = [-1] * 20
r = [-1] * 20

val = []
n = 0
ans = 1
vis = [0] * (1 << 17) 

def solve(state):
    global ans

    if vis[state]:
        return None

    vis[state] = 1
    wolf, num = 0, 0

    for i in range(n):
        if state & (1 << i):
            print(f"state & (1 << i): {bin(state)[2:]} & {bin(1 << i)[2:]} -> {bin(state & (1 << i))[2:]}")
            num += 1
            wolf += val[i]
    
    if 2 * wolf >= num:
        return None

    ans = max(ans, num - wolf)

    for i in range(n):
        if not state & (1<<i):
            continue
        # print(f"state | (1 << i): {state} | {1 << i} -> {state | (1 << i)}")
        if l[i] != -1:
            solve(state | (1<<l[i]))
        
        if r[i] != -1:
            solve(state | (1<<r[i]))


def solution(info, 	edges):
    global n, val
    n = len(info)
    val = info[:]

    for u, v in edges:
        if l[u] == -1:
            l[u] = v
        else:
            r[u] = v

    solve(1)
    
    return ans


if __name__ == "__main__":
    print("1번")
    # print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])) # 5
    print("2번")
    print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])) # 5