# 위장
# 각 카테고리에서 고르는 경우를
# 카테고리의 아이템수 + 1(안 고르는 경우) 로 나타내어 곱한 뒤
# 모든 카테고리에서 안 고른 경우 (1)을 제외시켜준다.


def solution(clothes):
    closet = {}

    # creating wardrobe
    for item in clothes:
        if item[1] not in closet.keys():
            closet[item[1]] = [item[0]]
        else:
            closet[item[1]].append(item[0])

    # pick one from each category
    # not picking is an option,
    # but not wearing anything is not an option
    #  -> picking at least one in total!
    # if there are 3 items, calculate assuming there are 4 items = not wearing from that category

    combo = 1
    for key in closet.keys():
        combo *= len(closet[key]) + 1

    return combo - 1


# clothes = [
#     ["yellow_hat", "headgear"],
#     ["blue_sunglasses", "eyewear"],
#     ["green_turban", "headgear"],
# ]
# 5

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# 3


print(solution(clothes))
