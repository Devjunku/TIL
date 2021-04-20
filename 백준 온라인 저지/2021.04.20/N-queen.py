def is_diag(idx, c):
    for i in range(idx):
        if idx - i  == abs(c-column[i]):
            return True

    return False

def Tracking(idx):
    global cnt

    if idx == N:
        cnt += 1
        return

    for i in range(N):

        if row[i]:
            continue

        if is_diag(idx, i):
            continue

        row[i] = 1
        column[idx] = i
        Tracking(idx+1)
        row[i] = 0


N = int(input())

column = [0 for _ in range(N)]
row = [0 for _ in range(N)]
cnt = 0
Tracking(0)
print(cnt)