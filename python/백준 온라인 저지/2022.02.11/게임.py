x, y = map(int, input().split())

if x == y:
    print(-1)
else:
    left = 1
    right = x
    winp = int((y/(x+y))*100)
    while left <= right:
        mid = (left + right) // 2
        print(f"새로운 승률: {int(((y+mid)/(x+y+mid))*100)}, 원래 승률: {winp}")
        print(f"mid: {mid}")
        if int(((y+mid)/(x+y+mid))*100) > winp:
            right = mid - 1
        else:
            left = mid + 1

print(right)
        