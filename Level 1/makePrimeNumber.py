# 소수 만들기

def solution(nums):
    answer = 0

    nums.sort()

    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                for l in range(2, temp):
                    if temp % l == 0:
                        break
                    elif l == temp - 1:
                        answer += 1

    return answer

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
