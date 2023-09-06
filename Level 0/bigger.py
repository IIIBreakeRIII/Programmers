# 머쓱이보다 키 큰 사람

def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1

    return answer
