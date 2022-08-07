# 1트
# from itertools import product

# def solution(numbers, target):
#     if target > sum(numbers):
#         return 0

#     answer = 0

#     p = product([-1, 1], repeat=len(numbers))

#     for each in p:
#         # print(each)
#         total = 0

#         for i in range(len(numbers)):
#             total += each[i] * numbers[i]

#         if total == target:
#             answer += 1

#     return answer

# 2트
from collections import deque


def solution(numbers, target):
    numbers = deque(numbers)
    queue = deque([0])
    while numbers:
        nextNum = numbers.popleft()
        # level
        ql = len(queue)
        print("nextNum:", nextNum)
        for i in range(ql):
            curr = queue.popleft()
            print("curr:", curr)
            queue.extend([curr + (-1 * nextNum), curr + nextNum])
        print(queue)

    return queue.count(target)


# 3트
# def solution(numbers, target):
#     answer = 0
#     n = len(numbers)


# 인덱스를 저장하는 방식


# print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
