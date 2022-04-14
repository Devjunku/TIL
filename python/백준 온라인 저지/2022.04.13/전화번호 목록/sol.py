import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    call_number = [input().strip() for _ in range(n)]
    call_number.sort()

    for i in range(1, n):
        prev, nxt = len(call_number[i-1]), len(call_number[i])
        if prev <= nxt:
            if call_number[i-1] in call_number[i][0:prev]:
                print("NO")
                break
    else:
        print("YES")