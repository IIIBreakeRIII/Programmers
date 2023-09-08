# N개의 최소 공배수

import math

def solution(arr):
    answer = arr[0]
    for num in range(1, len(arr)):
        answer = (answer * arr[num]) // math.gcd(answer, arr[num])
         
    return answer

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([2, 4, 8]))
print(solution([2, 3, 4, 10]))
