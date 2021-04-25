'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
'''

N = int(input())
seq = list(map(int, input().split()))

start = 0
while start <= N:
    mid = (start+N)//2
    if seq[mid] == mid:
        break

    if seq[mid] < mid:
        start = mid+1
    else:
        N = mid-1

if seq[mid] == mid:
    print(mid)
else:
    print(-1)