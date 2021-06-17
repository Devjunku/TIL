import sys

sys.stdin = open('sample_sample_input.txt')

def BT(h, w, c):
    global max_value, mapping


    if h+2 > H:
        BT(0, w+1, c)

    if h+2 > H or w+2 > W:
        if max_value < c:
            max_value = c
        return


    flag = 1

    # 칩을 만들 수 있는지 확인
    for i in range(h, h+2):
        for j in range(w, w+2):
            if mapping[i][j]:
                flag = 0
                break
        if not flag:
            break

    # 만들 수 있으면
    if flag:
        # 만들고
        for i in range(h, h+2):
            for j in range(w, w+2):
                mapping[i][j] = 1

        # 그 상태로 bfs
        BT(h+2, w, c+1)

        # 원 상태로 돌려주고
        for i in range(h, h+2):
            for j in range(w, w+2):
                mapping[i][j] = 0
        
    # 한 칸 밀어서 bfs
    else:
        BT(h+1, w, c)


T = int(input())

for t in range(1, T+1):
    # H는 세로, W는 가로
    H, W = map(int, input().split())
    mapping = [list(map(int, input().split())) for _ in range(H)]
    max_value = -sys.maxsize
    BT(0, 0, 0) # 1, 2번째 인자 좌표, 3번째 인자 갯수
    print(max_value)