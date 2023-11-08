# 문자열 잘라서 정렬하기

def solution(myString):
    answer = list(filter(None, myString.split("x")))
    return sorted(answer)
