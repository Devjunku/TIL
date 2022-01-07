from pandas import DataFrame
import sys


arr = [[0 for _ in range(8)] for _ in range(8)]

dic_col = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8
}

dxy = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1)
}


input = sys.stdin.readline

king, stone, n = map(str, input().split())
king_col, king_row = dic_col[king[0]]-1, int(king[1])-1
stone_col, stone_row = dic_col[stone[0]]-1, int(stone[1])-1
n = int(n)

arr[king_row][king_col] = 1
arr[stone_row][stone_col] = 2

for _ in range(n):
    direct = input().strip()
    dx, dy = dxy[direct]
    if 0 <= king_row + dx < 8 and 0 <= king_col + dy < 8:
        if arr[king_row + dx][king_col + dy] != 2:
            arr[king_row][king_col] = 0
            arr[king_row + dx][king_col + dy] = 1
            king_row, king_col = king_row + dx, king_col + dy
        else:
            if 0 <= stone_row + dx < 8 and 0 <= stone_col + dy < 8:
                # 킹 움직임
                arr[king_row][king_col] = 0
                arr[king_row + dx][king_col + dy] = 1
                king_row, king_col = king_row + dx, king_col + dy
                # 돌 움직임
                arr[stone_row][stone_col] = 0
                arr[stone_row + dx][stone_col + dy] = 2
                stone_row, stone_col = stone_row + dx, stone_col + dy

trace_col = {y:x for x, y in dic_col.items()}
print(DataFrame(arr))
# for i in range(8):
#     for j in range(8):
#         if arr[i][j] == 1:
#             str(trace_col[j+1])





