from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
sx, sy = n//2, n//2
shark_dx = [-1, 1, 0, 0]
shark_dy = [0, 0, -1, 1]

ans = {
    1: 0,
    2: 0,
    3: 0
}

arr_point = []

# 좌표를 저장하는게 이득
def circuit_arr(sx, sy, n):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    flag = 0
    move_size = 1

    while True:
        if move_size != n-1:
            for _ in range(2):
                for _ in range(move_size):
                    nx, ny = sx + dx[flag%4], sy + dy[flag%4]
                    arr_point.append((nx, ny))
                    sx, sy = nx, ny
                flag += 1
            move_size += 1
        else:
            for _ in range(3):
                for _ in range(move_size):
                    nx, ny = sx + dx[flag%4], sy + dy[flag%4]
                    arr_point.append((nx, ny))
                    sx, sy = nx, ny
                flag += 1
            break

# 각 좌표별 구슬 값을 q에 저장
q = deque([])
def black_full():
    for r, c in arr_point:
        if arr[r][c] != 0:
            q.append(arr[r][c])

# 구슬 폭발
def explosive():
    stack = []
    data = [q[0]]
    toggle = False
    for i in range(1, len(q)):
        if not data:
            data.append(q[i])
            continue
        
        if data[-1] == q[i]:
            data.append(q[i])
        else:
            if len(data) >= 4:
                toggle = True
                ans[data[-1]] += len(data)
            else:
                stack.extend(data)
            data.clear()
            data.append(q[i])

    if len(data) >= 4:
        toggle = False
        ans[data[-1]] += len(data)
        data.clear()
    stack.extend(data)
    return (deque(stack), toggle)

# 구글 복사
def copy_marble():
    stack = []
    data = [q[0]]
    for i in range(1, len(q)):
        if not data:
            data.append(q[i])
            continue
        
        if data[-1] == q[i]:
            data.append(q[i])
        else:
            stack.append(len(data))
            stack.append(data[-1])
            data.clear()
            data.append(q[i])
    if data:
        stack.append(len(data))
        stack.append(data[-1])
    return deque(stack)

# 모두 0이면 그냥 탈출
if sum(sum(arr[i]) for i in range(n)) == 0:
    print(0)
    exit()

circuit_arr(sx, sy, n)
for _ in range(m):
    d, s = map(int, input().split())
    d -= 1

    q.clear()
    # TODO 1.구글 파괴
    for i in range(1, s+1):
        nx, ny = sx + shark_dx[d]*i, sy + shark_dy[d]*i
        arr[nx][ny] = 0

    # TODO 2. 빈자리 채우기
    black_full()

    # TODO 3. 터지는지 확인
    q, toggle = explosive()
    while toggle:
        q, toggle = explosive()
    
    # # TODO 4. 구슬 복사
    if q: q = copy_marble()

    # TODO 5. arr 수정
    for i in range(n**2-1):
        if i < len(q):
            arr[arr_point[i][0]][arr_point[i][1]] = q[i]
        else:
            arr[arr_point[i][0]][arr_point[i][1]] = 0

res = 0
for key, value in ans.items():
    res += key*value

print(res)