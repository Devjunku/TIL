# 출처: https://baaaaaaaaaaaaaaaaaaaaaaarkingdog.tistory.com/1003?category=916869
import sys
sys.setrecursionlimit(10**6)

l = [0] * 10005 # 왼쪽 노드
r = [0] * 10005 # 오른쪽 노드
x = [0] * 10005 # 시험장의 응시 인원
p = [-1] * 10005 # 부모 노드의 번호
n = 0 # 노드의 수
root = 0 # 루트

cnt = 0 # 그룹의 수

# cur : 현재 보는 노드 번호, lim : 그룹의 최대 인원 수
def dfs(cur, lim):
    global cnt

    lv = 0
    if l[cur] != -1: lv = dfs(l[cur], lim)
    rv = 0
    if r[cur] != -1: rv = dfs(r[cur], lim) # 왼쪽 자리에서 넘어오는 인원 수

    # 1. 왼쪽 자식 트리에서 넘어오는 인원과, 오른쪽 자식 트리에게 넘어오는 인원의 합이 lim를 넘지 않는 경우
    if x[cur] + lv + rv <= lim:
        return x[cur] + lv + rv
    
    # 2. 왼쪽 자식 트리에서 넘어오는 인원과, 오른쪽 자식 트리에게 넘어오는 인원 중 작은 것을 합해도 lim을 넘지 않는 경우
    if x[cur] + min(lv, rv) <= lim:
        cnt += 1
        return x[cur] + min(lv, rv)
    
    # 1, 2 둘다 속하지 않는 경우 그룹은 2개를 추가해야함 (왼쪽 자식 트리 그룹 + 오른쪽 자식 트리 그룹)
    cnt += 2
    return x[cur]


def solve(lim):
    global cnt
    cnt = 0
    dfs(root, lim)
    cnt += 1 # 맨 마지막에 남은 인원은 그룹을 지어야 함
    return cnt


def solution(k, num, links):
    global root

    n = len(num)

    for i in range(n):
        l[i], r[i] = links[i]
        x[i] = num[i]
        if l[i] != -1: p[l[i]] = i
        if r[i] != -1: p[r[i]] = i
    
    for i in range(n):
        if p[i] == -1:
            root = i
            break
    
    st = max(x)
    en = 10 ** 8

    while st < en:
        mid = (st + en) // 2
        if solve(mid) <= k:
            en = mid
        else:
            st = mid + 1

    return st


if __name__ == "__main__":
    print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
    print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
    print(solution(2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
    print(solution(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))



