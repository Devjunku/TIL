# 반만 통과!

from copy import deepcopy

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = 0
M = 0
# 4에 하나라도 갈 수 있는가? 좌표를 출력 아무대도 못하면 False 출력
def is4d(x, y, reverse, board):
    possible = []
    for i in range(4):
        nx, ny = x + delta[i][0], y + delta[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                possible.append([nx, ny, distance([nx, ny], reverse)])
    if possible != []:
        return sorted(possible, key=lambda x: x[2])
    return False

def whowin(aloc, bloc, board):

    while True:
        possible = is4d(aloc[0], aloc[1], bloc, board)
        if possible == False:
            return "B"

        board[aloc[0]][aloc[1]] = 0
        aloc = [possible[0][0], possible[0][1]]
        
        if board[bloc[0]][bloc[1]] == 0:
            return "A"

        possible = is4d(bloc[0], bloc[1], aloc, board)
        if possible == False:
            return "A"

        board[bloc[0]][bloc[1]] = 0
        bloc = [possible[-1][0], possible[-1][1]]
   
        if board[aloc[0]][aloc[1]] == 0:
            return "B"


# 두 좌표의 거리
def distance(aloc, bloc):
    return abs(aloc[0]-bloc[0]) + abs(aloc[1]-bloc[1])


def solution(board, aloc, bloc):
    global N, M

    N = len(board)
    M = len(board[0])
    board1 = deepcopy(board)
    aloc1 = deepcopy(aloc)
    bloc1 = deepcopy(bloc)

    winner = whowin(aloc1, bloc1, board1)
    cnt = 0

    while True:
        
        possible = is4d(aloc[0], aloc[1], bloc, board)
        if possible == False:
            break

        board[aloc[0]][aloc[1]] = 0
        aloc = [possible[0][0], possible[0][1]]
        cnt += 1
        
        if board[bloc[0]][bloc[1]] == 0:
            break

        possible = is4d(bloc[0], bloc[1], aloc, board)
        if possible == False:
            break

        board[bloc[0]][bloc[1]] = 0
        if winner == "B":
            bloc = [possible[0][0], possible[0][1]]
        else:
            bloc = [possible[-1][0], possible[-1][1]]           
        cnt += 1
        
        if board[aloc[0]][aloc[1]] == 0:
            break

    return cnt
    
if __name__ == "__main__":
    print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
    print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
    print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
    print(solution([[1]], [0, 0], [0, 0]))