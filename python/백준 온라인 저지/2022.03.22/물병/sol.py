import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0
while True:
    number = 0
    for i in range(0, 1000):
        if n & (1 << i):
            number += 1
        
        if n < (1 << i):
            break
    
    if number <= k:
        break
    else:
        cnt += 1
        number += 1

print(cnt)