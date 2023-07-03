# 나머지가 1이 되는 수 찾기

def solution(n):
    new_n = n - 1
    answer = 0
    for i in range(2, new_n + 1):
        if new_n % i == 0:
            answer = i
            break
    
    return answer
