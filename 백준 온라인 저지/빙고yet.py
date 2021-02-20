from sys import stdin

arr1 = []
for _ range(5):
    arr1.append(list(map(int, stdin.readline().rstrip().split())))

arr2 = []
for _ range(5):
    arr2.append(list(map(int, stdin.readline().rstrip().split())))

cnt = 1
while True:
    for i in range(5):
        for j in range(5):
            for r in range(5):
                for n in range(5):
                    if arr2[i][j] == arr1[r][c]:
                        arr1[r][c] = 0
                    if cnt > 5:
                        bingo = 0
                        diag1 = 0
                        col = 0
                        for s1 in range(5):
                            if sum(arr1[s1]) = 0
                                bingo += 1
                            diag1 += arr1[s1][s1]
                            diag2 += arr1[4-s1][4-s1]
                            for s2 in range(5):
                                col += arr[s2][s1]    
                        if diag1 == 0:
                            bingo += 1
                        if diag2 == 0:
                            bingo += 1
                        if col == 0:
                            bingo += 1
    if bingo == 3:
        break
    cnt += 1
print(cnt)

