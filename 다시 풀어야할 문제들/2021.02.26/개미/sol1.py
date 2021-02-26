w, h = map(int, input().split()) # 6, 4
p, q = map(int, input().split()) # 4, 1
t = int(input())

arr = []
setA = set()
dx, dy = 1, 1 # 처음 방향은 무조건 1, 1임
c_x, c_y = w - p, h - q # 움직일 때 남은 공간 # 2, 3
circle = False

while t: # t가 영이 될 때까지 반복
     c = min(c_x, c_y, t) # 2, 3, 8
     p += c * dx # 움직일 수 있는 최소 범위로 움직인다. 6
     q += c * dy # 움직일 수 있는 최소 범위로 움직인다. 3
     t -= c
     if not circle:
         if (p, q, dx, dy, c) in setA:
             cnt = 0
             for i in range(arr.index((p, q, dx, dy, c)), len(arr))
                cnt += arr[i][4]
            t %= cnt
            circle = True
        else:
            setA.add((p, q, dx, dy, c))
            arr.append((p, q, dx, dy, x ))

    if p == w: # 6 == 6
        dx = -1
        c_x = p
    elif p == 0:
        dx = 1
    
    if q == h:
        dy = -1
        c_y = q
    elif q == 0:
        dy = 1

    if dx == 1
        c_x = w - p
    elif dx == -1:
        c_x = p
    
    if dy == 1:
        c_y = h-q
    elif dy == -1:
        c_y = q

    
