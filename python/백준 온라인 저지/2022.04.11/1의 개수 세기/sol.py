import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def f(n):
     
    cnt = 0
    k = 0

    while 2**k <= n:
        
        p = 2 ** (k+1)

        p_cnt  = (n+1)//p

        cnt += p_cnt * (p//2)

        left = (n+1) % p

        cnt += max(0, left-p//2)

        k += 1
    
    return cnt

print(f(b)-f(a-1))


# from math import comb, log2

# arr = [1] * 55

# for i in range(1, 54):
#     print(2**i)

# def combination_1num(exponen):
#     answer = 1

#     for i in range(1, exponen+1):
#         answer += (i+1)*comb(exponen,i)

#     return answer

# for i in range(1, 55):
#     arr[i] = combination_1num(i)
# # print(arr)

# for i in range(1, 55):
#     arr[i] += arr[i-1]

# print(arr)
# print(log2(a), log2(b))