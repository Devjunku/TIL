num1, num2 = map(str, input().split())
A = int(''.join(list(reversed(num1))))
B = int(''.join(list(reversed(num2))))
print(A) if A > B else print(B)

