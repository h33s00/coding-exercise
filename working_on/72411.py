# 메뉴 리뉴얼


def solution(orders, course):
    answer = []
    new = []

    for i in range(len(orders)):
        for k in range(1, len(orders)):
            answer.append(set(list(orders[i])) & set(list(orders[k])))

    for item in answer:
        if answer.count(item) >= 2:
            new.append(item)
            answer.remove(item)

    return new


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# orders = ["XYZ", "XWY", "WXA"]

course = [2, 3, 4]
print(solution(orders, course))
