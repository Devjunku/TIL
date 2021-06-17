from sys import stdin
height = []
for _ in range(9):
    height.append(int(stdin.readline().rstrip()))

sum_h = sum(height)

for i in range(8):
    for j in range(i+1, 9):
        if sum_h - (height[i] + height[j]) == 100:
            ele_1 = height[i]
            ele_2 = height[j]
            break
height.remove(ele_1)
height.remove(ele_2)

height.sort()
for h in height:
    print(h)