from sys import stdin

w, h = map(int, stdin.readline().rstrip().split())

nums = int(stdin.readline().rstrip())

row = [0]
col = [0]
for _ in range(nums):
    i, num = map(int, stdin.readline().rstrip().split())
    if i == 0:
        col.append(num)
    else:
        row.append(num)
        
col.append(h)
col.sort()
row.append(w)
row.sort()

r = row[1] - row[0]
c = col[1] - col[0]
for i in range(2, len(col)):
    if c < col[i] - col[i-1]:
        c = col[i] - col[i-1]
    
for j in range(2, len(row)):
    if r < row[j] - row[j-1]:
        r = row[j] - row[j-1]

print(c*r)



