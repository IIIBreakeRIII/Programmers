# 원소들의 곱과 합

def solution(num_list):
    sum = 0
    time = 1

    for i in num_list:
        sum += i
        time *= i

    if sum ** 2 > time:
        return 1
    else:
        return 0
