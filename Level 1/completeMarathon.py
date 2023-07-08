# 완주하지 못한 선수

# 런타임 에러
# def solution(participant, completion):
#     
#     for i in range(len(completion)):
#         for j in range(len(participant)):
#             if completion[i] == participant[j]:
#                 participant[j] = " "
#                 break
#     
#     no_complete = []
#     for k in range(len(participant)):
#         if participant[k] == " ":
#             pass
#         else:
#             no_complete.append(participant[k])
#     
#     print(no_complete)
#     return no_complete

def solution(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
