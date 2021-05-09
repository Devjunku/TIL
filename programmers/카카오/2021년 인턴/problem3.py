from collections import deque

def solution(n, k, cmd):
    
    q = deque(cmd)
    numbers = [1] * n
    stack = []
    loc = k
    while q:
        cmd = q.popleft()
        if cmd == 'Z':
            a = stack.pop()
            numbers[a] = 1
            n += 1
            continue
        elif cmd == 'C':
            if loc == n-1:
                numbers[loc] = 0
                stack.append(loc)
                while True:
                    if not numbers[loc]:
                        loc -= 1
                    else:
                        break
            else:
                numbers[loc] = 0
                stack.append(loc)
                while True:
                    if not numbers[loc]:
                        loc += 1
                    else:
                        break
            continue
        c, num = cmd.split()
        num = int(num)
        if c == 'U':
            while num:
                if numbers[loc]:
                    loc -= 1
                    num -= 1
                else:
                    loc -= 1
            continue
        elif c == 'D':
            while num:
                if numbers[loc]:
                    loc += 1
                    num -= 1
                else:
                    loc += 1
    ans = ''
    for n in numbers:
        if n:
            ans += 'O'
        else:
            ans += 'X'
    
    return ans

if __name__ == "__main__":
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
    print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))