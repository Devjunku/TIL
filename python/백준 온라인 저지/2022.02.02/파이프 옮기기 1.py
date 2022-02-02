from pprint import pprint
import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = [[[0 for i in range(N)] for _ in range(N)] for _ in range(N)]
result[0][0][1] = 1

pprint(result)

for i in range(2, N):
    if board[0][i] == 0:
        result[0][0][i] = result[0][0][i-1]

for i in range(1, N):
    for j in range(2, N):
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0:
            result[2][i][j] = result[0][i-1][j-1] + result[1][i-1][j-1] + result[2][i-1][j-1]
        
        if board[i][j] == 0:
            result[0][i][j] = result[0][i][j-1] + result[2][i][j-1]
            result[1][i][j] = result[1][i-1][j] + result[2][i-1][j]

answer = [result[x][N-1][N-1] for x in range(3)]
print(sum(answer))