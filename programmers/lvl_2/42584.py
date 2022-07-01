# 주식가격

# 이중 FOR문 풀이
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         time = 0
#         for k in range(i + 1, len(prices)):
#             time += 1
#             if prices[i] > prices[k]:
#                 break
#         answer.append(time)
#     return answer

# 스택을 사용한 풀이
def solution(prices):
    maxStack = []  # [인덱스, 값]
    result = [None] * len(prices)
    for i, v in enumerate(prices):
        print("Stack: ", maxStack)
        # 첫 요소이거나 가격이 유지/상승한 경우
        if len(maxStack) == 0 or v >= maxStack[-1][1]:
            maxStack.append([i, v])
        # 가격이 하락한 경우
        elif v < maxStack[-1][1]:
            while len(maxStack) != 0 and v < maxStack[-1][1]:
                temp = maxStack.pop()
                result[temp[0]] = i - temp[0]
            maxStack.append([i, v])

    # 가격이 떨어지지 않은 것들
    if len(maxStack) != 0:
        while len(maxStack) != 0:
            temp = maxStack.pop()
            result[temp[0]] = (len(prices) - 1) - temp[0]
    return result


prices = [5, 8, 6, 2, 4, 1]
# result // [3, 1, 1, 2, 1, 0]

prices = [1, 2, 3, 2, 3]
# result // [4, 3, 1, 1, 0]
print(solution(prices))
