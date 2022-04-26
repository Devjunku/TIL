from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우에 따라서 합쳐져야 한다.

def merge_element(narr, d):

    if d == 0: # 위
        for i in range(n):
            q = deque([])
            for j in range(n):
                if narr[j][i] != 0:
                    q.append(narr[j][i])
                    narr[j][i] = 0
            
            k = 0
            q_num = len(q)
            result_data = []
            while k < q_num:
                if k == q_num - 1:
                    result_data.append(q[k])
                    break
                if q[k] == q[k+1]:
                    result_data.append(q[k]+q[k+1])
                    k += 2
                else:
                    result_data.append(q[k])
                    k += 1

            for j in range(len(result_data)):
                narr[j][i] = result_data[j]

    elif d == 1: # 아래 
        for i in range(n):
            q = deque([])
            for j in range(n-1, -1, -1):
                if narr[j][i] != 0:
                    q.append(narr[j][i])
                    narr[j][i] = 0
            
            k = 0
            q_num = len(q)
            result_data = []
            while k < q_num:
                if k == q_num - 1:
                    result_data.append(q[k])
                    break
                if q[k] == q[k+1]:
                    result_data.append(q[k]+q[k+1])
                    k += 2
                else:
                    result_data.append(q[k])
                    k += 1

            for j in range(len(result_data)):
                narr[n-j-1][i] = result_data[j]
    elif d == 2: # 오른쪽
        for i in range(n):
            q = deque([])
            for j in range(n-1, -1, -1):
                if narr[i][j] != 0:
                    q.append(narr[i][j])
                    narr[i][j] = 0
            
            k = 0
            q_num = len(q)
            result_data = []
            while k < q_num:
                if k == q_num - 1:
                    result_data.append(q[k])
                    break
                if q[k] == q[k+1]:
                    result_data.append(q[k]+q[k+1])
                    k += 2
                else:
                    result_data.append(q[k])
                    k += 1

            for j in range(len(result_data)):
                narr[i][n-j-1] = result_data[j]
    elif d == 3: # 왼쪽
        for i in range(n):
            q = deque([])
            for j in range(n):
                if narr[i][j] != 0:
                    q.append(narr[i][j])
                    narr[i][j] = 0
            
            k = 0
            q_num = len(q)
            result_data = []
            while k < q_num:
                if k == q_num - 1:
                    result_data.append(q[k])
                    break
                if q[k] == q[k+1]:
                    result_data.append(q[k]+q[k+1])
                    k += 2
                else:
                    result_data.append(q[k])
                    k += 1

            for j in range(len(result_data)):
                narr[i][j] = result_data[j]
    return narr


def find_max(arr):
    res = 0
    for i in range(n):
        res = max([res] + arr[i])
    return res


answer = 0
def _2048Game(arr, number):
    global answer

    if number >= 5:
        answer = max(answer, find_max(arr))
        return

    
    for i in range(4):
        new_arr = merge_element(deepcopy(arr), i)
        _2048Game(new_arr, number+1)

_2048Game(arr, 0)
print(answer)