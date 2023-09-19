# 카드 뭉치

def check(cards_list):
    for i in range(len(cards_list)):
        if i != cards_list[i]:
            return 0

    return 1


def solution(cards1, cards2, goal):

    cards1_index = []
    cards2_index = []

    for i in goal:
        if i in cards1:
            cards1_index.append(cards1.index(i))
        elif i in cards2:
            cards2_index.append(cards2.index(i))

    if check(cards1_index) == 1 and check(cards2_index) == 1:
        return "Yes"
    else:
        return "No"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
