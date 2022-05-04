# 가장 큰 수

# 첫번째 시도
# 순열로 모든 조합을 구한 후 정렬

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


# 시간초과 ! 순열로 풀 수 없다 !!

# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9, 0]
numbers = [30, 3021]
# numbers = [15, 151]
# numbers = [0, 0, 70]
# numbers = [0, 0, 0, 0]
# numbers = [0, 0, 1, 0, 0]
# numbers = [9, 998]

print(solution(numbers))
