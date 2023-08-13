# 소수 찾기
# 에라토스테네스의 체

# 시간 초과
# def solution(n):
#     answer = 0
#     
#     for i in range(2, n + 1):
#         if i == 2:
#             answer += 1
#         else:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#                 else:
#                     if j == i - 1:
#                         if i % j != 0:
#                             answer += 1
#     return answer

import math

def prime_num(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if prime_num(i):
            answer += 1
    return answer

print("answer =", solution(10))
print("answer =", solution(5))
