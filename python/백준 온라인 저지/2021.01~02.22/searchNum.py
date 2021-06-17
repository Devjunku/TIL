while True:
    s = input()
    if s == '0':
        break
    if s == s[::-1]:
        print('yes')
    else:
        print("no")



if s == s[::-1] and s != '0':
    print("yes")
elif s == '0':
    print()
else:
    print("no")

