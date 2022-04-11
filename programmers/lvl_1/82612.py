# 부족한 금액 계산하기


def solution(price, money, count):
    total_cost = 0
    for i in range(1, count + 1):
        total_cost += price * i

    answer = money - total_cost
    if answer >= 0:
        return 0
    else:
        return abs(answer)


print(solution(3, 20, 4))
