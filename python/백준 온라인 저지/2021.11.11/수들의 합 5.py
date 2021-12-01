N = int(input())

l = 1
r = 1
s = 1
cnt = 0

while r <= N:
    if s == N:
        cnt += 1
    if s + r + 1 <= N:
        s += r + 1
        r += 1
    else:
        s -= l
        l += 1
        
print(cnt)