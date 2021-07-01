import sys
N, M = map(int, input().split())

mapping = [list(map(int, input().split())) for _ in range(N)]

# data of cctv
cctv = []
cctv_n = 0
for i in range(N):
    for j in range(M):
        if mapping[i][j] != 0 and mapping[i][j] != 6:
            cctv.append((i, j))
            cctv_n += 1

# 사각지대를 구하는 함수
def nonesee():
    global mapping

    cnt = 0
    for i in range(N):
        for j in range(M):
            if mapping[i][j] == 0:
                cnt += 1

    return cnt

# 감시 시작
max_ = sys.maxsize
def cctving(n, cctv_n):
    global mapping

    if not cctv_n:
        cnt = nonesee()
        if cnt < max_:
            max_x = cnt
        return
    
    for i in range(n, cctv_n):
        if cctv[i]




