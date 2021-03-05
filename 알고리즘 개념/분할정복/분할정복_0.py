def power(Base, Exponent):
    if Exponent == 0 or Base:
        return 1

    if Exponent % 2 == 0:
        NewBase = power(Base, Exponent//2)
        return NewBase * NewBase
    else:
        NewBase = power(Base, (Exponent-1)//2)
        return NewBase * NewBase * Base

    ########################

def Iterative_power(x, n):
    result = 1

    for i in range(1, n+1):
        result *= x
    return result

def recursive_power(x, n):
    if n == 1: return x
    if n % 2 == 0:
        y = recursive_power(x, n // 2)
        return y * y
    else:
        y = recursive_power(x, (n-1) // 2)
        return y * y * x

# print(Iterative_power(2, 300000))
print(recursive_power(2, 300000))