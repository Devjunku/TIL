import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
land = [False for _ in range(N+1)]
duck = [int(input()) for _ in range(Q)]


def explore(loc, duck_want):

    global is_end

    if loc > duck_want: return

    if land[loc]:
        print(f"답 {loc}")
        is_end = True
        return

    if loc == duck_want:
        land[loc] = True
        print(f"답 0")
        return
    
    explore(loc*2, duck_want)

    if is_end: return

    explore(loc*2 + 1, duck_want)

    if is_end: return

    


for d in duck:
    is_end = False
    explore(1, d)
    print("   ")