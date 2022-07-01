# 파괴되지 않은 건물


def solution(board, skill):
    answer = 0

    # 분석
    for turn in skill:
        # print("타입: ", turn[0])
        # print("범위1: ", turn[1:3])
        # print("범위2: ", turn[3:5])
        # print("degree: ", turn[-1])
        if turn[0] == 1:
            sign = -1
        elif turn[0] == 2:
            sign = 1

        perform(board, sign, turn[1:3], turn[3:5], turn[-1])

    print(board)

    # 효율성...
    # 1 이상인 것 세기

    for each in board:
        answer += len([x for x in each if x > 0])
        print(answer)

    return answer


def perform(
    board,
    sign,
    start,
    end,
    degree,
):
    for r in range(start[0], end[0] + 1):
        for c in range(start[1], end[1] + 1):
            # print(r, c)
            board[r][c] += sign * degree


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board, skill))
