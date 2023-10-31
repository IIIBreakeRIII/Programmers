# 배열 회전시키기

from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
        
    return list(numbers)
