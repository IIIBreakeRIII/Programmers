# 기사단원의 무기

# 시간 초과
# # 약수 개수 구하기
# # 만약에 limit보다 크면, 반복문 종료 후 power를 반환
# def count_divisor(num, limit, power):
    
#     # 자기 자신을 더해놓고 시작
#     count = 1
    
#     for i in range(1, num):
#         if num % i == 0:
#             count += 1
        
#         if count > limit:
#             return power
    
#     return count

# def solution(number, limit, power):
    
#     answer = 0
    
#     # number까지 숫자 모두 확인하면서 answer에 더해줌
#     for num in range(1, number + 1):
#         answer += count_divisor(num, limit, power)
        
#     return answer



# 제곱수일 경우 약수의 개수는 홀수개
# 따라서 count * 2해준 후 -1
def square_num_count(num, limit, power):
    
    sqrt_num = int(num ** (1/2))
    count = 0
    
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            count += 1
            
    count = count * 2 - 1
    
    if count > limit:
        return power
    else:
        return count

# 제곱수 아닐 경우 약수의 개수는 짝수개
def none_square_num_count(num, limit, power):
    
    sqrt_num = int(num ** (1/2))
    count = 0
    
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            count += 1
            
    count = count * 2
    
    if count > limit:
        return power
    else:
        return count

# 제곱수인지 확인
def check_sqrt(num):
    
    if num ** (1/2) == int(num ** (1/2)):
        return True
    else:
        return False

# 약수의 개수 구하기
# 약수 구하는 알고리즘
# num을, 1부터 sqrt(num)까지의 수로 나눠서 나누어 떨어지는지 확인 후
# 나중에 2배 해주면 됨
def solution(number, limit, power):
    
    answer = 0
    
    for i in range(1, number + 1):
        # 제곱수일 경우
        if check_sqrt(i) == True:
            answer += square_num_count(i, limit, power)
        # 제곱수가 아닐 경우
        else:
            answer += none_square_num_count(i, limit, power)
            
    return answer
            
