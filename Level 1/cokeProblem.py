# 콜라 문제

def solution(a, b, n):
    
    answer = 0

    while n // a != 0:
        if n // a == 0:
            break
        answer += (n // a) * b
        n = n - (n // a * a) + ((n // a) * b)

    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))
