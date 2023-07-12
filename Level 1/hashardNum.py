# 하샤드 수

def solution(x):
    list_x = list(map(str, str(x)))
    
    tempNum = 0

    for i in range(len(list_x)):
        tempNum = tempNum + int(list_x[i])
    
    if x % tempNum == 0:
        return True
    else:
        return False

solution(10)
solution(12)
solution(11)
solution(13)
