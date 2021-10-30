import sys
max_num = sys.maxsize

A, B = input().split()

lenA = len(A)
lenB = len(B)
for i in range(0, lenB-lenA+1):
    cnt = 0
    for j in range(lenA):
        if A[j] != B[j+i]:
            cnt += 1
    if cnt < max_num:
        max_num = cnt

print(max_num)
