# 피로도
# 순열을 이용한 문제

from itertools import permutations

def solution(k, dungeons):
    
    answer = 0
    
    for permut in permutations(dungeons, len(dungeons)):
        hp = k
        count = 0
        
        for lst in permut:
            if hp >= lst[0]:
                hp -= lst[1]
                count += 1
        
        if count > answer:
            answer = count    
        
    return answer
