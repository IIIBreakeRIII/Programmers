# 부분 문자열 이어 붙여 문자열 만들기

def solution(my_strings, parts):
    answer = ''
    index = 0
    for i in my_strings:
        answer += i[parts[index][0]:parts[index][1] + 1]
        index += 1

    return answer
