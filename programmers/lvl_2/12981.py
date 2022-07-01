# 영어 끝말잇기


def checkValidity(prevWord, currWord):
    if prevWord[-1] == currWord[0]:
        return True
    else:
        return False


# 1트
# def solution(n, words):
#     lost = [0, 0]
#     player = {}  # Player # / Passed Round
#     prevWord = ""

#     for i in range(len(words)):
#         currWord = words[i]
#         p = (i % n) + 1
#         currRound = (i // n) + 1
#         print(currRound)

#         # Initialize First Round
#         if prevWord == "":
#             player[p] = currRound

#         else:
#             if not checkValidity(prevWord, currWord):
#                 print("WRONG!")
#                 lost = [p, currRound]
#                 break
#             else:
#                 if currWord in words[:i]:
#                     print("ALREADY SAID!")
#                     lost = [p, currRound]
#                     break
#                 else:
#                     player[p] = currRound

#         prevWord = currWord
#         # print(player)

#     return lost

# 2트
def solution(n, words):
    lost = [0, 0]
    prevWord = ""

    for i in range(len(words)):
        currWord = words[i]
        p = (i % n) + 1
        currRound = (i // n) + 1
        print(p, currRound)

        if prevWord != "" and not checkValidity(prevWord, currWord):
            print("WRONG!")
            lost = [p, currRound]
            break
        else:
            if currWord in words[:i]:
                print("ALREADY SAID!")
                lost = [p, currRound]
                break

        prevWord = currWord

    return lost


n = 3
words = [
    "tank",
    "kick",
    "know",
    "wheel",
    "land",
    "dream",
    "mother",
    "robot",
    "tank",
]
# result // [3,3]

# n = 5
# words = [
#     "hello",
#     "observe",
#     "effect",
#     "take",
#     "either",
#     "recognize",
#     "encourage",
#     "ensure",
#     "establish",
#     "hang",
#     "gather",
#     "refer",
#     "reference",
#     "estimate",
#     "executive",
# ]
# # result // [0,0]

# n = 2
# words = ["hello", "one", "even", "never", "now", "world", "draw"]
# # result // [1,3]


print(solution(n, words))
