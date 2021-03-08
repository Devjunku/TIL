N = int(input())
N_list = list(map(int, input().split()))
stack = []
ans = [-1 for _ in range(N)]
for i in range(len(N_list)):
    while stack and N_list[stack[-1]] < N_list[i]:
        ans[stack.pop()] = N_list[i]
    stack.append(i)
print(*ans)
        
    
