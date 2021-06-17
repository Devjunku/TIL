'''
_###_
_____
_#_#_
##A#B
'''

arr = [list(input()) for _ in range(4)]

mapping = [[0 for _ in range(5)] for _ in range(4)]

for i in range(4):
    for j in range(5):
        if arr[i][j] == '_':
            mapping[i][j] = int(-1e9)
        elif arr[i][j] == 'A':
            start = [i, j]
            mapping[i][j] = 0
        elif arr[i][j] == 'B':
            end = [i, j]
            mapping[i][j] = 0
        else:
            mapping[i][j] = -1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dp(start, c):

    x, y = start[0], start[1]
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 5 and mapping[nx][ny] != -1:
            if mapping[nx][ny] > mapping[x][y] + 1:
                mapping[nx][ny] = mapping[x][y] + 1
            else:
                





    pass

