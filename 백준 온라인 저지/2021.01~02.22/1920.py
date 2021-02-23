import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))
A.sort()
T = int(sys.stdin.readline().rstrip())
M = list(map(int,sys.stdin.readline().rstrip().split()))

def binarySearch(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True # 검색 성공
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False # 검색 실패


for i in range(T):
    if binarySearch(A, M[i]):
        print(1)
    else:
        print(0)
    
    
    





