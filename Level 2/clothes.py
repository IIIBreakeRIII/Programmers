# 의상

def solution(clothes):

    clothes_list = {}
    answer = 1

    for i in clothes:
        if i[1] in clothes_list.keys():
            clothes_list[i[1]] += 1
        else:
            clothes_list[i[1]] = 1

    for i in clothes_list:
        answer = answer * (clothes_list[i] + 1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
