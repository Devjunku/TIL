from sys import stdin
from pandas import DataFrame
arr1 = []
for _ in range(5):
    arr1.append(list(map(int, stdin.readline().rstrip().split())))

arr2 = []
for _ in range(5):
    arr2.extend(list(map(int, stdin.readline().rstrip().split())))

print(arr2)

for i in range(1, 12):
    arr1[(arr2[i-1]-1)//5][(arr2[i-1]-1)%5] = 0
    print('i:', i)
    print(DataFrame(arr1))

for i in range(12, 26):
    arr1[(arr2[i-1]-1)//5][(arr2[i-1]-1)%5] = 0
    
    bingo = 0
    diag1 = 0
    diag2 = 0
    for k in range(5):
        diag1 += arr1[k][k]
        diag2 += arr1[4 - k][k]

    if diag1 == 0:
        bingo += 1
        
    if bingo == 3:
        break
        
    if diag2 == 0:
        bingo += 1

    if bingo == 3:
        break

    for j in range(5):     
        row = 0
        col = 0
        
        if bingo == 3:
            break

        for k in range(5):
            row += arr1[j][k]
            col += arr1[k][j]

        if row == 0:
            bingo += 1
        
        if bingo == 3:
            break

        if col == 0:
            bingo += 1
        
        if bingo == 3:
            break
    
    print('i:', i, 'bingo:', bingo)
    print(DataFrame(arr1))

    if bingo == 3:
        print(i)
        break
        
    
        
