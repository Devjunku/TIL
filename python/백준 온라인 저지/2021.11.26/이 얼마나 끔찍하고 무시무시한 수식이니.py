string = input()

dic = {
    "ZERO": "0",
    "ONE": "1",
    "TWO": "2",
    "THREE": "3",
    "FOUR": "4",
    "FIVE": "5",
    "SIX": "6",
    "SEVEN": "7",
    "EIGHT": "8",
    "NINE": "9"
}

dic_ans = {
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "0": "NINE",
    "-": "-",
    "+": "+",
    "x": "x",
    "/": "//"
}
result_string = []
num_string = ""
for s in string:
    if num_string in dic.keys():
        result_string.append(dic[num_string])
        num_string = ""
    if s in ["+", "-", "/", "x"]:
        if s == "x": result_string.append("*")
        elif s == "/": result_string.append("//")
        else: result_string.append(s)
        continue
    if s == "=":
        break
    num_string += s

print("".join(result_string) + "=")

result = eval("".join(result_string))
result_answer = []
for r in str(result):
    if r == "=":
        break
    result_answer.append(dic_ans[r])
print("".join(result_answer))
