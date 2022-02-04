import sys

def md(nx, ny, dx, dy): 
    return abs(nx-dx) + abs(ny-dy)


def is_go_to_festival(com_store, sh_x, sh_y, px, py):

    if md(sh_x, sh_y, px, py) <= 2000:
        return True

    while com_store:
        if md(sh_x, sh_y, px, py) > 2000:
            nx, ny, ncost = com_store.pop()
            if md(sh_x, sh_y, nx, ny) <= 2000:
                sh_x, sh_y = nx, ny
            else:
                return False
        else:
            return True

    if md(sh_x, sh_y, px, py) <= 2000:
        return True
    else:
        return False

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sh_x, sh_y = map(int, input().split())

    com_store = []
    for _ in range(n):
        cx, cy = map(int, input().split())
        com_store.append((cx, cy))
    

    px, py = map(int, input().split())

    if is_go_to_festival(com_store, sh_x, sh_y, px, py):
        print("happy")
    else:
        print("sad")