N, X = map(int, input().split())

data = list(map(int, input().split()))

for dat in data:
    if dat < X:
        print(dat, end = ' ')