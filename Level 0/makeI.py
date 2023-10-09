# I로 만들기

def solution(myString):
    answer = ""

    for i in myString:
        if ord(i) >= ord("a") and ord(i) <= ord("l"):
            answer += "l"
        else:
            answer += i

    return answer
