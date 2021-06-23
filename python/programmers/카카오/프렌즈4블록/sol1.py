def is2x2(m, n, board):
    answer = []
    for i in range(m-1):
        for j in range(n-1):
            temp = board[i][j]
            if temp == 0:
                continue
            if temp == board[i+1][j] and temp == board[i][j+1] and temp == board[i+1][j+1]:
                answer += [[i, j], [i+1, j], [i, j+1], [i+1, j+1]]
    return list(set(map(tuple, answer)))


def removeBlock(m, board, l):
    print(l)
    for i in l:
        print(board[i[0]])
        board[i[0]].pop(i[1])
    for j in range(m):
        if len(board[j]) < m:
            board[j] += [0] * (m - len(board[j]))
    return board
    

def solution(m, n, board):
    # print(board)
    # 행을 열로 전환
    board = list(map(list, zip(*board[::-1])))
    # print(board)
    m, n = n, m
    answer = 0
    while True:
        temp = is2x2(m, n, board)
        if temp == []:
            break
        answer += len(temp)
        board = removeBlock(m, board, sorted(temp, reverse = True))
    return answer
    

if __name__ == '__main__':
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))