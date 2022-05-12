import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
_max = max(arr)
_min = min(arr)

init = _max * _min
start = init

def comfirm():

    for a in arr:
        if start % a != 0:
            return True
    
    return False

while comfirm():
    start += init

print(start)