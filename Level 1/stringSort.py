# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    answer_temp = []

    for i in strings:
        answer_temp.append(i[n] + i)

    answer_temp.sort()
    
    for i in answer_temp:
        answer.append(i[1:])
                         
    return answer
