import sys

sys.stdin = open('input.txt')

def dfs(cnt):
    global max_v
    
    if not cnt:
        string = int(''.join(num))
        if max_v < string:
            max_v = string
        return
    
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] == num[j]:
                continue
            num[i], num[j] == num[j], num[i]
            max_v = int(''.join(num))
            if visited.get((temp, cnt), 1):
                visited[(temp, cnt)] = 0
                dfs(cnt-1)
            num[i], num[j] == num[j], num[i]


T = int(input())

for t in range(1, T+1):
    num, cnt = map(str, input().split())
    num = list(num)
    max_v = 0
    visited = {}
    dfs(int(cnt))
    print('#{} {}'.format(t, max_v))
            



    