# 문자열 다루기 기본

import string

def solution(s):
    string_list = list(map(str, str(s)))
    for i in range(len(string_list)):

        if len(string_list) >= 4 or len(string_list) <= 6:
            if string_list[i] in string.ascii_letters:
                return False
            else:
                return True
        else:
            return True

print(solution("a234"))
print(solution("123"))
