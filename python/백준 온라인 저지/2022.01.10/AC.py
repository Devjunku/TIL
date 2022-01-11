from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    command = list(input())
    cl = len(command)
    n = int(input())
    arr = deque([])
    string_arr = list(input())
    for i in range(1, 2*n+1, 2):
        arr.append(int(string_arr[i]))

    r_tf = True
    for i in range(cl):
        if command[i] == 'R':
            r_tf = not r_tf
        elif command[i] == 'D':
            if not command:
                print("error")
                continue
            elif r_tf:
                arr.popleft()
            elif not r_tf:
                arr.pop()

    if not command:
        continue
    else:
        if r_tf:
            print("여기!",arr)
        else:
            print("여기!",arr[::-1])
                
            



