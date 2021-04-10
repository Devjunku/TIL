N, r, c = map(int, input().split())
positive_int = list(range(0, 2**(2*N)))
res = -1
def div(positive_int, sx, ex, sy, ey):
    global res, r, c
    
    if sx == r and sy == c:
        res = positive_int[0]
        return
    elif sx == r and sy+1 == c:
        res = positive_int[1]
        return
    elif sx+1 == r and sy == c:
        res = positive_int[2]
        return
    elif sx+1 == r and sy+1 == c:
        res = positive_int[3]
        return

    if sx <= r < (sx+ex)//2 and sy <= c < (sy+ey)//2:
        div(positive_int[0:N//4], sx, (sx+ex)//2, sy, (sy+ey)//2)
    elif sx <= r < (sx+ex)//2 and (sy+ey)//2 <= c < ey:
        div(positive_int[N//4:2*(N)//4], sx, (sx+ex)//2, (sy+ey)//2, ey)
    elif (sx+ex)//2 <= r < ex and sy <= c < (sy+ey)//2:
        div(positive_int[2*(N)//4:3*(N)//4], (sx+ex)//2, ex, sy, (sy+ey)//2)
    else:
        div(positive_int[3*(N)//4:(N)], (sx+ex)//2, ex, (sy+ey)//2, ey)

div(positive_int, 0, 2**N, 0, 2**N)
print(res)
