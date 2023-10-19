# 외계행성의 나이

def solution(age):
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    answer = ''
    
    age_str = str(age)
    for i in age_str:
        answer += alpha[int(i)]
    
    return answer
