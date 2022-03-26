import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(n)]
# 만들 수 있는 조합을 생각해야 한다.
# 어떤 상태를 만들어서 조합시키면 어떻게 될까?


def bit_mask():
    result = 0
    for i in range(1 << n*m):
        total = 0
        for r in range(n):
            srow = 0
            for c in range(m):
                idx = r * m + c
                if i & (1 << idx) != 0:
                    srow = srow * 10 + arr[r][c]
                else:
                    total += srow
                    srow = 0
            total += srow

        for c in range(m):
            scol = 0
            for r in range(n):
                idx = r * m + c
                if i & (1 << idx) == 0:
                    scol = 10 * scol + arr[r][c]
                else:
                    total += scol
                    scol = 0
            total += scol
    
        result = max(result, total)
    
    return result

print(bit_mask())