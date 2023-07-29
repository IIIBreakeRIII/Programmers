# 3진법 뒤집기

def solution(n):
    arithmetic_list = []
    answer = 0
    while n >= 3:
        arithmetic_list.insert(0, n % 3)
        n = n // 3
    else:
        arithmetic_list.insert(0, n)

    for i in range(len(arithmetic_list)):
        answer += (3 ** i) * arithmetic_list[i]

    return answer
    
print(solution(45))
print(solution(125))
