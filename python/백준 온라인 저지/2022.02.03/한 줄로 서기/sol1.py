# 메모리 초과 및 시간 초과

import sys
input = sys.stdin.readline

n = int(input())
info = list(map(int, input().split()))
person = [i for i in range(1, n+1)]

def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for idx, ele in enumerate(arr):
        for P in permutation(arr[:idx] + arr[idx+1:], n-1):
            result += [[ele]+P]

    return result

per_list = permutation(person, n)

for l in per_list:
    line = [-1 for _ in range(n)]
    for i in range(n):
        if i == 0:
            line[l[i]-1] = 0
            continue
        else:
            cnt = 0
            for j in range(i-1, -1, -1):
                if l[i] < l[j]:
                    cnt += 1
            line[l[i]-1] = cnt

    toggle = False
    for a, b in zip(info, line):
        if a != b:
            toggle = True
            break
    
    if toggle:
        continue
    else:
        print(*l)
        break
