def circuit():
    global i, string, res

    word = ''
    while string[i] != '>':
        print(i)
        word += string[i]
        i += 1
    
    word += string[i]
    res += word
    return

def back():
    global i,string, res

    word = ''
    while i < len(string) or (string[i] != ' ' and string[i] != '<'):
        print(i)
        word += string[i]
        i += 1

    res += word[::-1]

    try:
        if string[i] == ' ':   
            res += ' '
    except:
        return

    return
    

string = input()

i = 0
res = ''
while i < len(string):
    if string[i] == '<':
        circuit()
        i += 1
    if string[i] != '<':
        back()
        i += 1

print(res)




