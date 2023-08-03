# 시저 암호

import string

def solution(n, s):
    answer = ''
    for index in list(n):
        if index == " ":
            answer += " "
        else:
            if index in string.ascii_lowercase:
                temp = string.ascii_lowercase.find(index) + s
                answer += string.ascii_lowercase[temp % 26]
            else:
                temp = string.ascii_uppercase.find(index) + s
                answer += string.ascii_uppercase[temp % 26]

    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
