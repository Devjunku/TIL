# 양치기 테케 3개...

import sys
sys.setrecursionlimit(100000)

cnt = 0

def dfs(info, s, graph, sheep, wolf):
    global cnt

    if wolf != 0:
        if wolf >= sheep:
            return

    if cnt < sheep:
        cnt = sheep

    for start in graph[s]:
        if info[start] == 1:
            info[start] = -1
            dfs(info, start, graph, sheep, wolf+1)
        elif info[start] == 0:
            info[start] = -1
            dfs(info, start, graph, sheep+1, wolf)


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for inf in edges:
        s, e = inf[0], inf[1]
        graph[s].append(e)
        graph[e].append(s)

    for i in range(len(info)):
        dfs(info, i, graph, 0, 0)
    
    return cnt


if __name__ == "__main__":
    print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
    print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))