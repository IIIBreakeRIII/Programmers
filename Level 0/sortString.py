# 문자열 정렬하기

def solution(my_string):
    lst = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    answer = []
    for i in my_string:
        if i in lst:
            answer.append(int(i))

    answer.sort()

    return answer
