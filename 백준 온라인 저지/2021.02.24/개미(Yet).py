
from pandas import DataFrame
from sys import stdin


def dontgo(p, q):
    global w, h
    if p < 0 or p > w+1 or q < 0 or q > h + 1:
        return 0
    else:
        return 1

dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]

def solution(p, q, arr, t):
    tm = 0
    while tm < t:
        for i in range(4):
            d_x = dx[i]
            d_y = dy[i]
            print(dontgo(p+d_x, q+d_y), p+d_x, q+d_y )
            while True:
                deter = dontgo(q, p)    
                if deter == 0:
                    break
                if deter == 1:
                    arr[q][p] = 1
                    p += d_x
                    q += d_y
                    print(DataFrame(arr))
                    tm += 1
                else:
                    break
    return [p,q]

w, h = map(int, stdin.readline().rstrip().split())
p, q = map(int, stdin.readline().rstrip().split())

arr = [[0 for _ in range(w+1)] for _ in range(h+1)]

print(DataFrame(arr))

t = int(stdin.readline().rstrip())

print(solution(p-1, q-1, arr, t))