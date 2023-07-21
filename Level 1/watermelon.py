# 수박수박수?

def solution(n):
    
    answer = ""

    for i in range(n):
        if i == 0 or i % 2 == 0:
            answer += "수"
        else:
            answer += "박"

    return answer

print(solution(3))
print(solution(4))
