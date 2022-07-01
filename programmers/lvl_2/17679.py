#  프렌즈4블록

# 지워질 것이 있는지 체크
def popCheck(m, n, board):
    toDelete = []
    for i in range(m - 1):
        for k in range(n - 1):
            # 1차 체크 : 양옆이 같은 세트가 존재?
            if board[i][k] == board[i][k + 1] and board[i][k] != "-":
                # 2차 체크 : 밑에 동일한 블록세트가 존재?
                if (
                    board[i][k] == board[i + 1][k]
                    and board[i][k] == board[i + 1][k + 1]
                ):
                    print("pops at: ", i, k)
                    # 지워져야 할 요소의 (2x2 의 왼쪽 상단) 인덱스 저장
                    toDelete.append([i, k])
    return toDelete


# popCheck(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])

# 블록이 터짐
def popBlock(board, toDelete):
    # pop
    popCount = 0
    for each in toDelete:
        i, k = each[0], each[1]
        for j in range(2):
            for p in range(2):
                if board[i + j][k + p] != "-":
                    board[i + j][k + p] = "-"
                    popCount += 1
        print("팡!!! \n", board)
    return popCount


# print(
#     popBlock(
#         [
#             ["-", "-", "-", "D", "E"],
#             ["-", "-", "-", "D", "E"],
#             ["C", "C", "B", "B", "F"],
#             ["C", "C", "B", "B", "F"],
#         ],
#         [[2, 0], [2, 2]],
#     )
# )

# 블록이 빈칸을 채움
def fallBlock(m, n, board):
    # fall
    for i in range(n):
        column = [item[i] for item in board]
        if "-" in column:
            numBlank = column.count("-")
            etc = []
            for each in column:
                if each != "-":
                    etc.append(each)
            # print(etc)
            # print(numBlank)
            for j in range(0, numBlank):
                board[j][i] = "-"
            for k in range(numBlank, m):
                board[k][i] = etc.pop(0)
    return board


# print(
#     fallBlock(
#         4,
#         5,
#         [
#             ["-", "-", "-", "D", "E"],
#             ["-", "-", "-", "D", "E"],
#             ["-", "-", "-", "-", "F"],
#             ["-", "-", "-", "-", "F"],
#         ],
#     )
# )


def solution(m, n, board):
    popCount = 0
    board = list(map(list, board))
    while True:
        print("-------------------------")
        print(board)
        checkResult = popCheck(m, n, board)
        # 더 이상 터질 것이 없다면 끝
        if len(checkResult) == 0:
            break
        else:
            popCount += popBlock(board, checkResult)
            print("gravity falls...")
            board = fallBlock(m, n, board)

    return popCount


# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
