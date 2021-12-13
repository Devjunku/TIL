def solution(s):

    num_dic = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    answer = []
    sub_string = []
    for string in s:
        if string.isdigit():
            answer.append(string)
        else:
            sub_string.append(string)

        key = "".join(sub_string)

        if key in num_dic.keys():
            answer.append(num_dic[key])
            sub_string = []

    return int("".join(answer))


if __name__ == "__main__":
    print(solution("one4seveneight"))
    print(solution("23four5six7"))
    print(solution("2three45sixseven"))
    print(solution("123"))