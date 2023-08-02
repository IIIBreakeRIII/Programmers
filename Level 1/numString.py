# 숫자 문자열과 영단어

def solution(s):
    string_list = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for string in string_list.items():
        s = s.replace(string[0], string[1])

    return int(s)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

