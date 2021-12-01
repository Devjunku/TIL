string = input()

def confirm_cute(string):
    if len(string) < 5:
        return "not cute"
    
    if string[-5:] == "driip":
        return "cute"
    
    return "not cute"

print(confirm_cute(string))