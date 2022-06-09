# 메뉴 리뉴얼

from itertools import combinations


def solution(orders, course):
    answer = []

    # 가능한 모든 조합 찾기
    combos = []
    for i in range(len(orders)):
        for k in range(1, len(orders)):
            if i == k:
                pass
            else:
                # print(i, k)
                # 두개의 주문의 합집합
                combi = set(orders[i]) & set(orders[k])
                # 단품 메뉴 두개이상인 경우만
                if len(combi) >= 2:
                    for n in course:
                        for x in combinations(combi, n):
                            # print(set(x))
                            if set(x) in combos:
                                # print("이미 있는뎁쇼?")
                                pass
                            else:
                                combos.append(set(x))

    print(f"후보: {combos}")

    menu = {}
    for item in combos:
        count = 0
        for order in orders:
            if all(x in list(order) for x in list(item)):
                count += 1
        menu["".join(sorted(list(item)))] = count

    print(f"카운트: {menu}")

    # find most-frequent value in course of n
    for n in course:
        temp = {}
        for key, val in menu.items():
            if len(key) == n:
                temp[key] = val
        if len(temp) != 0:
            mf = max(temp.values())
            for key, val in temp.items():
                if val == mf:
                    answer.append(key)

    print(f"정렬 전: {answer}")

    return sorted(answer)


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# orders = ["XYZ", "XWY", "WXA"]
# print(combos(orders))
# print(list(orders[0]))
# print(set(list(orders[0])) & set(list(orders[1])))
# print(set(orders[0]) & set(orders[1]))
course = [2, 3, 4]
# course = [2, 3, 5]
print(solution(orders, course))
