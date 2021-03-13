import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for t in range(1,T+1):
    W,H,N = map(int,input().split())
    x,y = map(int,input().split()) 
    cnt = 0
    for _ in range(N-1):
        nx, ny =map(int,input().split())
        if x == nx:
            cnt += abs(y-ny) 
        elif y == ny:
            cnt += abs(x-nx)
        elif (x < nx and y > ny) or (x > nx and y < ny):
            cnt += abs(x-nx) + abs(y-ny)
        else:
            cnt += max(abs(x-nx), abs(y-ny)) 
        x, y = nx, ny
    print("#{} {}".format(t, cnt))