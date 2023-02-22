# 자릿수 더하기

def solution(Num):
    NumList = list(map(int, str(Num)))
    answer = 0
    
    for i in range(len(NumList)):
        answer = answer + NumList[i]
        
    return answer
