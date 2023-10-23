# x 사이의 개수

def solution(myString):
    answer = []
    count = 0

    for i in range(len(myString)):
        if myString[i] != "x":
            count += 1
            if i == len(myString) - 1:
                answer.append(count)
        else:
            answer.append(count)
            count = 0
            if i == len(myString) - 1:
                answer.append(count)

    
    return answer

print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))
