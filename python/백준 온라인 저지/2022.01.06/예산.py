import sys
input = sys.stdin.readline

n = int(input())
r_list = list(map(int, input().split()))
r = int(input())

r_list.sort()

def find_r(r, r_list, n):
    s_r_list = sum(r_list)

    if s_r_list <= r:
        return max(r_list)
    
    mid = max(r_list)
    while True:
        res_r = 0
        idx = 0
        for i in range(n):
            if r_list[i] < mid:
                res_r += r_list[i]
            else:
                idx = i
                break
        
        res_r += ((n-idx) * mid)
        if res_r <= r:
            return mid
        else:
            mid -= 1

print(find_r(r, r_list, n))
