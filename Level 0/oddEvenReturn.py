# 홀짝에 따라 다른 값 반환하기

def solution(n):

    answer = 0

    if n % 2 == 0:
        for i in range(n + 1):
            if i % 2 == 0:
                answer += i ** 2

    else:
        for i in range(n + 1):
            if i % 2 == 1:
                answer += i

    return answer
