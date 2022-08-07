def solution(n):
    numList = [0, 1, 2, 4]
    answer = []  # 인덱스번째 자리에 해당하는 수
    decimalNum = n
    while decimalNum > 0:
        print(decimalNum)
        answer.append(decimalNum % 3)
        decimalNum = decimalNum // 3

    print(answer)


# 1 2 4 - 3^1
# 11 12 14 21 22 24 41 42 44 - 3^2
# 111 112 114
# 121 122 124
# 141 142 144 ... 444 - 3^3


solution(13)
