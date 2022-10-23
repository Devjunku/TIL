import sys
input = sys.stdin.readline

W, N = input().strip().split()
N = int(N)
arr = [list(input().strip().split()) for _ in range(N)]

def reverse_number(number):
    if number == "8":
        return "8"
    elif number == "1":
        return "1"
    elif number == "2":
        return "5"
    elif number == "5":
        return "2"
    
    return "?"


answer_arr = [[] for _ in range(N)]
# L OR R
if W == "L" or W == "R":
    for i in range(N):
        for j in range(N-1, -1, -1):
            answer_arr[i].append(reverse_number(arr[i][j]))
else:
    for i in range(N):
        for j in range(N):
            answer_arr[N-i-1].append(reverse_number(arr[i][j]))
    

for i in range(N):
    print(*answer_arr[i])