# 모르겠다.. 너무어렵네..

# 방향에 따라 이동했을 때, 좌표값
def changeDirection(direction, x, y, row_max, col_max, arr):
    x += direction[0]
    y += direction[1]
    if 0 <= x < row_max and 0 <= y < col_max: return (x, y)
    elif 0 <= x < row_max and (not 0 <= y < col_max): return (x, 0)
    else: return (0, y)

# 문자에 따른 바뀐 방향
def change(direction, x, y, arr):
    if arr[x][y] == "S": return direction
    elif arr[x][y] == "R":
        if direction[0] == 0 and direction[1] == 1: return (1, 0)
        elif direction[0] == 0 and direction[1] == -1: return (-1, 0)
        elif direction[0] == 1 and direction[1] == 0: return (0, -1)
        else: return (0, 1)
    elif arr[x][y] == "L":
        if direction[0] == 0 and direction[1] == 1: return (-1, 0)
        elif direction[0] == 0 and direction[1] == -1: return (1, 0)
        elif direction[0] == 1 and direction[1] == 0: return (0, 1)
        else: return (0, -1)

def solution(grid):

    arr = []
    row_max = len(grid)
    col_max = len(grid[0])
    for g in grid:
        arr.append(list(g))
    

    while True:
        g

    print(arr)

    
    return 

if __name__ == "__main__":
    print(solution(["SL","LR"]))
    print(solution(["S"]))
    print(solution(["R","R"]))