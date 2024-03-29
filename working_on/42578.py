# 위장
# 좆 구린 문제. 수학식 없으면 시간초과 되어 풀 수 없다.
# 시간초과를 제외하면 밑의 코드는 모든 테스트케이스를 통과한다.

from itertools import combinations


def solution(clothes):
    wardrobe = {}

    for item in clothes:
        if item[1] not in wardrobe:
            wardrobe[item[1]] = [item[0]]
        else:
            wardrobe[item[1]].append(item[0])

    # 카테고리의 갯수
    n = len(wardrobe.keys())

    print(wardrobe)

    answer = 0
    pc = []

    # 카테고리 갯수 별로 1~N개 선택 가능
    # 예) 모자+상의 (2), 모자+상의+하의 (3) 등
    for i in range(1, n + 1):
        pc.append(combinations(wardrobe.keys(), i))

    print(pc)

    for c in pc:
        # print(c)
        for combi in c:
            # print(combi)
            t = 1
            for cat in combi:
                t *= len(wardrobe[cat])
            answer += t

    return answer


# clothes = [["burberry", "outer"]]
clothes = [
    ["a", "face"],
    ["b", "eye"],
    ["c", "top"],
    ["d", "bottom"],
    ["e", "outer"],
    ["f", "face"],
]

# clothes = [
#     ["yellowhat", "headgear"],
#     ["bluesunglasses", "eyewear"],
#     ["green_turban", "headgear"],
# ]


# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

print(solution(clothes))
