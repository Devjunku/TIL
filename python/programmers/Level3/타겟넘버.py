from collections import deque

def solution(numbers, target):
    
    N = len(numbers) - 1
    q = deque([(numbers[0], 0), (- numbers[0], 0)])
    cnt = 0

    while q:
        value, idx = q.popleft()

        if idx == N:
            for v, i in q:
                if v == target:
                    cnt += 1
            break

        if idx + 1 <= N:
            q.append((value + numbers[idx+1], idx+1))
            q.append((value - numbers[idx+1], idx+1))

    return cnt
    

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))