# 1로 만들기

def solution(num_list):
    
    count = 0
    
    for num in num_list:
        while num != 1:
            if num % 2 == 0:
                num = num //2
                count += 1
            else:
                num = (num - 1) // 2
                count += 1
                
    return count
