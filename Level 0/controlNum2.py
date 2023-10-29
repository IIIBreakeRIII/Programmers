# 수 조작하기2

def solution(numLog):
    
    answer = ''
    num_list = {"w": 1, "s": -1, "d": 10, "a": -10}
    
    for i in range(0, len(numLog) - 1):
        result = numLog[i + 1] - numLog[i]
        for key, value in num_list.items():
            if value == result:
                answer += key
                break
        
    return answer
