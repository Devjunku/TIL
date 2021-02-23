t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    total = 0
    for _ in range(n):
        total = one
        one = one + zero
        zero = total
    print(zero, one)