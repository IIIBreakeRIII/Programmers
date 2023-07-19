# 제일 작은 수 제거하기

def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        temp = arr[0]
        for i in range(len(arr)):
            if temp > arr[i]:
                temp = arr[i]
            else:
                pass
        
        for j in range(len(arr)):
            if arr[j] == temp:
                del arr[j]
                break

        return arr

print(solution([4, 3, 2, 1]))
print(solution([10]))
