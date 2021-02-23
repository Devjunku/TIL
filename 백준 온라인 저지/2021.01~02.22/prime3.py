def prime_num(nums):
    if nums == 1:
        return False
    elif nums == 2:
        return True
    else:
        for i in range(2, int(nums**0.5)+1):
            if nums % i == 0:
                return False
        return True

n, m = map(int, input().split())

numbers = list(range(n , m+1))

for number in range(n, m+1):
    if prime_num(number):
        print(number)

# print(list(range(2, 2)))

n, m = map(int, input().split())
a = [False,False] + [True]*(m-1)
primes=[]
for i in range(n,m+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, m+1, i):
        a[j] = False

for prime in primes:
  print(prime)