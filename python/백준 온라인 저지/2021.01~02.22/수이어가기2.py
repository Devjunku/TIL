import sys

input = sys.stdin.readline

x = int(input())


def seq(a, b):
    li = [a, b]
    while li[-2]-li[-1] > -1:
        li.append(li[-2]-li[-1])
    
    return (len(li), li)

start = x // 2 
end = int(x * (2/3) + 1) + 1

max_len = 0
result_list = []
for i in range(start, end):
    res = seq(x, i)
    
    if res[0] > max_len:
        max_len = res[0]
        result_list = res[1]

print(max_len)
print(' '.join(list(map(str, result_list))))