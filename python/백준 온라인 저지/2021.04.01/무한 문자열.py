str1 = input()
str2 = input()


def confirm(str1, str2):

    if len(str1) > len(str2):
        str1, str2 = str2, str1

    len1 = len(str1)
    len2 = len(str2)

    len3 = len2 // len1

    if len1 == len2:
        if str1 == str2:
            return 1
        else:
            return 0
    else:
        if str1*len2 == str2*len1:
            return 1
        else:
            return 0

print(confirm(str1, str2))
        
            



        

