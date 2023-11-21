# 글자 지우기

def solution(my_string, indices):
    
    answer = list(my_string)
    
    for i in indices:
        answer[i] = ""
    
    return "".join(answer)
