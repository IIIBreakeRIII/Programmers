# 없는 숫자 더하기

def solution(numbers):
    result = 0
    
    for i in range(10):
        if i not in numbers:
            result = result + i

    print(result)
    return result

solution([1,2,3,4,6,7,8,0])
solution([5,8,4,0,6,7,9])
