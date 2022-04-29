import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())

arr = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d))


for _ in range(k):

    # TODO 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    new_arr = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            while arr[i][j]:
                m, s, d = arr[i][j].pop()
                nx, ny = (i+dx[d]*s)%n, (j+dy[d]*s)%n
                new_arr[nx][ny].append((m, s, d))


    # TODO 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    # 파이어볼은 4개의 파이어볼로 나누어진다.
    # 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다
    # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다
    # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
    # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    for i in range(n):
        for j in range(n):
            length = len(new_arr[i][j])
            if length >= 2:
                total_m = 0
                total_s = 0
                total_d = 0
                for m, s, d in new_arr[i][j]:
                    total_m += m
                    total_s += s
                    total_d += 1 if d % 2 else 0
                total_m //= 5
                total_s //= length

                new_arr[i][j].clear()

                if total_m == 0:
                    continue
                
                if total_d == length or total_d == 0:
                    for nd in [0, 2, 4, 6]:
                        new_arr[i][j].append((total_m, total_s, nd))
                else:
                    for nd in [1, 3, 5, 7]:
                        new_arr[i][j].append((total_m, total_s, nd))
    arr = new_arr[:]

total = 0
for i in range(n):
    for j in range(n):
        for m, s, d in arr[i][j]:
            total += m

print(total)