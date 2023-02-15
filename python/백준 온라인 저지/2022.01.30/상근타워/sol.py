import sys
input = sys.stdin.readline

target, m = map(int, input().split())

ele = [tuple(map(int, input().split())) for _ in range(m)]

answer = int(1000000001)
start = 1
end = target



for u, d in ele:
    init = int(1000000001)
    start = 1
    end = target
    while start <= end:
        mid = (start + end) // 2
        value = (u*mid) - (d*(target-mid))
        
        print(value, mid, target-mid)
        if value < init:
            init = value
            end = mid - 1
        else:
            start = mid + 1
    if init < 0: continue
    answer = min(answer, init)

# print(answer)
        


