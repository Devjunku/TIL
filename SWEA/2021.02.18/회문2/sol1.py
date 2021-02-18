import sys

sys.stdin = open('input.txt')


def t_mat(N_list):

    row = len(N_list)
    col = len(N_list[0])

    B = [[0 for _ in range(row)] for _ in range(col)]

    for i in range(row):
        for j in range(col):
            B[j][i] = N_list[i][j]
    return B

def pali(A):
    if A == A[::-1]:
        return True
    else:
        return False


for t in range(1,11):
    num = int(input())
    data = []
    for i in range(100):
        string = list(input())
        data.append(string)

    # print(data)
    max_num = 1

    for _ in range(2):
        data = t_mat(data)
        for k in range(1, len(data)):
            for j in range(len(data)):
                for i in range(len(data) - k + 1):
                    if pali(data[j][i:i + k]) and max_num < len(data[j][i:i + k]):
                        max_num = len(data[j][i:i + k])
    print('#{} {}'.format(t, max_num))




# arr = [1, 2, 3, 4, 5, 6, 7]
#
# for k in range(1, len(arr)):
#     for i in range(len(arr)-k+1):
#         print(arr[i:i+k])





