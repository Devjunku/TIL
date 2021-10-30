max_idx = 0
max_value = 0

for i in range(1, 10):
    value = int(input())
    if value > max_value:
        max_value = value
        max_idx = i

print(max_value)
print(max_idx)