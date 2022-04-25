import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 하나씩 조사할 때
# 비어 있는 칸 중에서
# 인접한 칸 중 가장 좋아하는 사람이 많은 칸 중
# 인접한 칸 중 가장 빈칸도 많은 칸 중
# 행과 열 순으로 정렬한 배열 중 하나의 원소를 뽑아서 update

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

student = []
student_preference = {}
for _ in range(n**2):
    number, _1, _2, _3, _4 = map(int, input().split())
    student_preference[number] = [_1, _2, _3, _4]
    student.append(number)
student = student[::-1]

empty = []
while student:
    sn = student.pop()
    # TODO
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0: continue

            like_cnt = 0
            empty_cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if not (0 <= nx < n and 0 <= ny < n): continue

                if arr[nx][ny] == 0: empty_cnt += 1
                elif arr[nx][ny] in student_preference[sn]: like_cnt += 1

            empty.append((like_cnt, empty_cnt, i, j))
    
    empty.sort(key=lambda x : (-x[0], -x[1], x[2], x[3]))
    arr[empty[0][2]][empty[0][3]] = sn
    empty.clear()

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if arr[nx][ny] in student_preference[arr[i][j]]:
                cnt += 1

        if cnt == 1: ans += 1
        elif cnt == 2: ans += 10
        elif cnt == 3: ans += 100
        elif cnt == 4: ans += 1000

print(ans)