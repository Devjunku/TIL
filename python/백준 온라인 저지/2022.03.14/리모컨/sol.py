import sys
input = sys.stdin.readline

target_channel = int(input())
broken_button_num = int(input())

if broken_button_num != 0:
    broken_buttons = list(map(int, input().split()))
else:
    broken_buttons = []

broken = {
    i: False for i in range(10)
}

for button in broken_buttons:
    broken[button] = True

if target_channel == 100:
    print(0)
else:
    start = abs(target_channel - 100)
    for i in range(1000000):
        for s in str(i):
            if broken[int(s)]:
                break
        else:
            start = min(start, len(str(i)) + abs(target_channel - i))

    print(start)
