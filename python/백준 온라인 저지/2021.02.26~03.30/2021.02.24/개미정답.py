w, h= map(int,input().split())
p, q= map(int,input().split())
t= int(input())
 
arr= []
setA= set()
dx, dy= 1,1
c_x, c_y= w- p, h- q
circle= False
while t:
    c = min(c_x, c_y, t)
    p += c* dx
    q += c* dy
    t -= c
    if not circle:
        if (p, q, dx, dy, c)in setA:
            cnt= 0
            for i in range(arr.index((p, q, dx, dy, c)),len(arr)):
                cnt+= arr[i][4]
            t %= cnt
            circle= True
        else:
            setA.add((p, q, dx, dy, c))
            arr.append((p, q, dx, dy, c))
 
    if p== w:
        dx= -1
        c_x= p
    elif p== 0:
        dx= 1
 
    if q== h:
        dy= -1
        c_y= q
    elif q== 0:
        dy= 1
 
    if dx== 1:
        c_x= w- p
    elif dx== -1:
        c_x= p
 
    if dy== 1:
        c_y= h- q
    elif dy== -1:
        c_y= q
 


출처: https://tkql.tistory.com/66 [싸비]