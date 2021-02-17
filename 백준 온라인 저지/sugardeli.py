n = int(input())

div = n // 5

while div >= 0:
    if (n - div*5) % 3 == 0:
        print((n - div*5) // 3 + div)
        break
    else:
        div -= 1
        if div < 0:
            print(-1)

