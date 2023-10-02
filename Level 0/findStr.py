# 원하는 문자열 찾기

def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0
