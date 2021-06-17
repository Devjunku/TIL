from sys import stdin  

for _ in range(4):
    ract = list(map(int, stdin.readline().rstrip().split()))

    r1 = ract[:2]
    r3 = ract[2:4]
    r5 = ract[4:6]
    r7 = ract[6:]

    r2 = [r1[0], r3[1]]
    r4 = [r3[0], r1[1]]
    r6 = [r5[0], r7[1]]
    r8 = [r7[0], r5[1]]

    print(r1, r2, r3, r4, r5, r6, r7, r8)

    if r1[0] < r5[0] < r3[0]:
        print('a')
    elif
        print('b')
    elif
        print('c')
    else:
        print('d')
    


