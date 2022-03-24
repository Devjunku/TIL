from pprint import pprint
import sys
input = sys.stdin.readline

n = int(input())
vote_local = [list(map(int, input().split())) for _ in range(n)]

s = 0
for i in range(n):
    s += sum(vote_local[i])


def gerrymandering(x, y, d1, d2):
    people = [0, 0, 0, 0, 0]
    arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(d1+1):
        arr[x+i][y-i] = 5
        arr[x+d2+i][y+d2-i] = 5
            
    for i in range(1, d2+1):
        arr[x+i][y+i] = 5
        arr[x+d1+i][y-d1+i] = 5


    # 1구역    
    for i in range(0, x+d1):
        for j in range(0, y+1):
            if arr[i][j] == 5:
                break
            people[0] += vote_local[i][j]

    # 2구역
    for i in range(0, x+d2+1):
        for j in range(n-1, y, -1):
            if arr[i][j] == 5:
                break
            people[1] += vote_local[i][j]


    # 3구역
    for i in range(x+d1, n):
        for j in range(0, y-d1+d2):
            if arr[i][j] == 5:
                break
            people[2] += vote_local[i][j]

    # 4구역
    for i in range(x+d2+1, n):
        for j in range(n-1, y-d1+d2-1, -1):
            if arr[i][j] == 5:
                break
            people[3] += vote_local[i][j]
 
    people[4] = s - sum(people)

    return max(people) - min(people)

answer =  int(1e9)
for i in range(n-2):
    for j  in range(1, n-1):
        x, y = i, j
        for d2 in range(1, n):
            for d1 in range(1, n):

                if not ((0 <= x+d1 < n) and (0 <= x+d2 < n) and (0 <= x+d1+d2 < n) and (0 <= y-d1 < n) and (0 <= y+d2 < n) and (0 <= y+d2-d1 < n)):
                    continue

                answer = min(gerrymandering(x, y, d1, d2), answer)

print(answer)