
import math
import sys

input = sys.stdin.readline

n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[] for _ in range(37)]
dp[0] = matrix
def matrix_multiply(matrix1, matrix2):
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
                new_matrix[i][j] %= 1000
    return new_matrix

for i in range(1, 37):
    dp[i] = matrix_multiply(dp[i-1], dp[i-1])


unit_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    unit_matrix[i][i] = 1

while b != 0:
    a = int(math.log2(b))
    unit_matrix = matrix_multiply(unit_matrix, dp[a])
    b -= 2**a

for i in range(n):
    print(*unit_matrix[i])

# def dfs(n):
#     if n == 1:
#         return matrix
    
#     if n % 2 == 1:
#         return matrix_multiply(dfs(n//2), dfs(n//2+1))
#     else:
#         return matrix_multiply(dfs(n//2), dfs(n//2))


# answer = dfs(b)