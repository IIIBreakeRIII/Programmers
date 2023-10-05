# 문자열 바꿔서 찾기

def solution(myString, pat):

    answer = ''

    for i in myString:
        if i == "A":
            answer += "B"
        else:
            answer += "A"

    if pat in answer:
        return 1
    else:
        return 0
