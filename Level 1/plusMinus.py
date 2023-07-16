# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]

    return answer
