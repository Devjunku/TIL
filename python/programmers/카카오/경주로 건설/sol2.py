dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, d, cost, N, board):

    matrix = [[0xffffff] * N for _ in range(N)]
    matrix[r][c] = 0

    Q = [(r, c, d, cost)]
    while Q:
        cur_r, cur_c, cur_direct, cost = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if cur_direct == i:
                temp_cost = cost + 100
            else:
                temp_cost = cost + 600

            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                if matrix[nr][nc] > temp_cost:
                    matrix[nr][nc] = temp_cost
                    Q.append((nr, nc, i, temp_cost))

    return matrix[N-1][N-1]


def solution(board):
    N = len(board)
    answer = min(bfs(0, 0, 1, 0, N, board), bfs(0, 0, 3, 0, N, board))
    return answer


if __name__ == '__main__':
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))
    print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
    print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
    print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))