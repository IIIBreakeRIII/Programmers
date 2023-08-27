# 피보나치 수

def solution(n):

    fibo_list = [0, 1, 1]

    for i in range(3, n + 1):
        fibo_list.append(fibo_list[i - 2] + fibo_list[i - 1])

    return fibo_list[-1] % 1234567

print(solution(5))
