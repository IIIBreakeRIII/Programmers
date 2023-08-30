# 영어 끝말잇기

def solution(n, words):
    
    player = 0      # 누군지
    turn = 0        # 차례
    stop_words = 0  # 어디서 멈췄는지
    temp_list = []
    
    for i in range(1, len(words)):

        temp_list.append(words[i - 1])

        temp_word_1 = list(words[i - 1])
        temp_word_2 = list(words[i])

        if temp_word_1[len(temp_word_1) - 1] != temp_word_2[0]:     # 끝말잇기 성립 안하면
            stop_words = i + 1

            if stop_words % n != 0:
                turn = stop_words // n + 1
            else:
                turn = stop_words // n

            if stop_words % n == 0:
                player = n
            else:
                player = stop_words % n

            return [player, turn]

        else:

            for j in temp_list:
                if words[i] == j:                                   # 똑같은 단어 얘기하면
                    stop_words = i + 1

                    if stop_words % n != 0:
                        turn = stop_words // n + 1
                    else:
                        turn = stop_words // n


                    if stop_words % n == 0:
                        player = n
                    else:
                        player = stop_words % n

                    return [player, turn]

    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
