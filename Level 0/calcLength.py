# 길이에 따른 연산

def solution(num_list):
    answer = 1
    if len(num_list) <= 10:
        for i in num_list:
            answer *= i
    else:
        answer = 0
        for i in num_list:
            answer += i

    return answer
