def solution(board, skill):

    n = len(board)
    m = len(board[0])
    d = [[0] * 1003 for _ in range(1003)]

    for v in skill:
        kind, r1, c1, r2, c2, degree = v
        if kind == 1: degree = -degree

        d[r1][c1] += degree
        d[r1][c2+1] -= degree
        d[r2+1][c1] -= degree
        d[r2+1][c2+1] += degree


    for i in range(1, n):
        for j in range(m):
            d[i][j] += d[i-1][j]
    
    for i in range(n):
        for j in range(1, m):
            d[i][j] += d[i][j-1]
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if d[i][j] + board[i][j] > 0:
                ans += 1
    
    return ans

if __name__ == "__main__":
    print(solution([[5,5,5,5,5],[5,5,5,5,5], [5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
    print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))