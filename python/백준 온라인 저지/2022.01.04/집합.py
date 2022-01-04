import sys

m = int(sys.stdin.readline())

S = set()
for _ in range(m):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        if command[0] == "all":
            S = set(i for i in range(1, 21))
        else:
            S.clear()
    else:
        f, number = command[0], command[1]

        if f == "add":
            S.add(number)
        elif f == "toggle":
            if number in S:
                S.discard(number)
            else:
                S.add(number)
        elif f == "check" :
            if number in S:
                print(1)
            else:
                print(0)
        elif f == "remove":
            S.discard(number)
