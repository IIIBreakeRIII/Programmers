# 숨어있는 숫자의 덧셈

def solution(my_string):
    answer = 0
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in my_string:
        if i in num:
            answer += int(i)

    return answer
