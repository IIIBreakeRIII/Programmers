# 특정 문자 제거하기

def solution(my_string, letter):

    temp = my_string
    answer = ''

    for i in my_string:
        if i == letter:
            temp = my_string.replace(i, " ")

    for i in range(len(temp)):
        if temp[i] == " ":
            pass
        else:
            answer += temp[i]

    return answer

print(solution("abcdef", 'f'))
