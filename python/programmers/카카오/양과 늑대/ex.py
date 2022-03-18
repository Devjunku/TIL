state = 1
n = 10

print(1 << 17)
for i in range(n):
    print(f"state & (1 << i): {state} & {1 << i} -> {state & (1 << i)}")
        