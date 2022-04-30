# 가장 큰 수


# 첫번째 시도
from itertools import permutations


def solution(numbers):
    candidates = []
    p = permutations(numbers, len(numbers))
    for each in p:
        c = ""
        for i in range(len(each)):
            c += str(each[i])
        candidates.append(c)
    cand_i = list(map(int, candidates))
    answer = str(max(cand_i))

    return answer


# numbers = [6, 10, 2]
# numbers = [0, 0, 0, 0]
# numbers = [3, 30, 34, 5, 9, 0]
# 34, 3, 30 / 34, 3, 31, / 35, 34, 3
# numbers = [9, 998]
numbers = [7, 3999999, 3, 30, 38, 340, 389, 8]
# numbers = [9, 9, 67300000, 439825, 4385042]
print(solution(numbers))
