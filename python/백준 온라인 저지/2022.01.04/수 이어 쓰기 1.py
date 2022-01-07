import sys

number = int(sys.stdin.readline().strip())
i = 1
answer = 0

while True:
    if 10**i <= number: answer += ((10**i) - (10**(i-1))) * i
    else:
        answer += (number - (10**(i-1)) + 1) * i
        break
    i += 1

print(int(answer))