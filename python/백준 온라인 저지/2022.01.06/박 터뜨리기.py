def sol():
    n, k = map(int, input().split())

    mini = k*(k+1) // 2

    if mini > n:
        return -1
    
    if (n - mini) % k  == 0:
        return k - 1
    else:
        return k


print(sol())
            

