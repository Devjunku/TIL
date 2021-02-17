from sys import stdin
N, M = map(int, stdin.readline().rstrip().split())
Coins = []
for _ in range(N):
    Coins.append(int(stdin.readline().rstrip()))
total = 0
for i in range(len(Coins)-1,-1,-1):
    if M // Coins[i] != 0:
        total += M // Coins[i]
        M = M % Coins[i]
print(total)

