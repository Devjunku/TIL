import sys
input = sys.stdin.readline

def potion(V, A):
    return (1 - (1 - V) * (1 - A))

N = int(input())
potions = list(map(int, input().split()))
V = 0
for p in potions:
    V = potion(V, p/100)
    print(f"{V*100:.6f}")