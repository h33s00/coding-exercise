def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        index = move - 1
        for tier in board:
            if tier[index] != 0:
                # 칸이 비어있지 않다면
                if len(basket) == 0:
                    basket.append(tier[index])
                else:
                    if tier[index] == basket[-1]:
                        basket.pop()
                        answer += 1
                    else:
                        basket.append(tier[index])
                tier[index] = 0
                break

    return answer * 2
