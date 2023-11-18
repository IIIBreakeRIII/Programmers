# 세로 읽기

def solution(my_string, m, c):
    
    answer = ''
    
    for i in range(len(my_string) // m):
        answer += my_string[(c - 1) + (m * i)]
        
    return answer
