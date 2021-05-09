nums_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3', 
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def solution(s):
    
    ans = ''
    nums_string = ''
    for i in s:
        if i.isdigit():
            ans += i
        else:
            nums_string += i
        
        if nums_string in nums_dict.keys():
            ans += nums_dict[nums_string]
            nums_string = ''
        
    return int(ans)


if __name__ == "__main__":
    print(solution("one4seveneight"))
    print(solution("23four5six7"))
    print(solution("2three45sixseven"))
    print(solution("123"))