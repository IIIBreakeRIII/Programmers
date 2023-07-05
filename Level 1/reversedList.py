# 자연수 뒤집어 배열로 만들기

def solution(n):    
    answer = []
    n_list = list(map(str, str(n)))
    
    for i in reversed(range(len(n_list))):
        answer.append(int(n_list[i]))
        
    return answer

solution(12345)
