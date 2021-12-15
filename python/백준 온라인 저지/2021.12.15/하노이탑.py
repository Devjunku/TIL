n = int(input())

def recurive_funtion(n, a, b, c):
    if n == 1:
        print(a, c, sep=" ")
    else:
        recurive_funtion(n-1, a, c, b)
        recurive_funtion(1, a, b, c)
        recurive_funtion(n-1, b, a, c)

print(2**n-1)
if n <= 20:
    recurive_funtion(n, 1, 2, 3)