# 폰켓몬

def solution(nums):
    
    mon_type = {}
    take = len(nums) // 2

    for i in nums:
        if i not in mon_type.keys():
            mon_type[i] = 0

    for i in nums:
        mon_type[i] += 1


    if len(mon_type) <= take:
        return len(mon_type)
    else:
        return take

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3,3,3,2,2,2]))
