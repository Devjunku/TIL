
import sys
sys.stdin = open('sample_input.txt')

def TF(ex_list, N):
    # 행렬 부분
    for i in range(N):
        for j in range(N-4):
            if ex_list[i][j]=='o' and ex_list[i][j+1]=='o' and ex_list[i][j+2]=='o' and ex_list[i][j+3]=='o' and ex_list[i][j+4]=='o':
                return True
            if ex_list[j][i]=='o' and ex_list[j+1][i]=='o' and ex_list[j+2][i]=='o' and ex_list[j+3][i]=='o' and ex_list[j+4][i]=='o':
                return True
            # print('i:', i, 'j:', j)
    
    # 대각선 부분
    for i in range(N-4):
        for j in range(N-4):
                # print(i,j)
            if ex_list[i][j]=='o' and ex_list[i+1][j+1]=='o' and ex_list[i+2][j+2]=='o' and ex_list[i+3][j+3]=='o' and ex_list[i+4][j+4]=='o':
                return True
            if ex_list[i][N-j-1]=='o' and ex_list[i+1][N-j-2]=='o' and ex_list[i+2][N-j-3]=='o' and ex_list[i+3][N-j-4]=='o' and ex_list[i+4][N-j-5]=='o':
                return True 

    return False

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        arr.append(list(input()))
    
    if TF(arr, N):
        print('#{} {}'.format(t, 'YES'))
    else:
        print('#{} {}'.format(t, 'NO'))

    