# 타겟 넘버

# 1트 - 라이브러리를 사용 - 성공
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

# 2트 - BFS - 테케 1,2 시간초과
# from collections import deque

# def solution(numbers, target):
#     numbers = deque(numbers)
#     queue = deque([0])
#     while numbers:
#         nextNum = numbers.popleft()
#         # level
#         ql = len(queue)
#         print("nextNum:", nextNum)
#         for i in range(ql):
#             curr = queue.popleft()
#             print("curr:", curr)
#             queue.extend([curr + (-1 * nextNum), curr + nextNum])
#         print(queue)

#     return queue.count(target)


# 3트 - Iterative DFS - 성공
def solution(numbers, target):
    result = []
    stack = [[0, 0]]  # 시작값, 탐색할 인덱스

    while stack:
        curr, idx = stack.pop()
        if idx == len(numbers):
            result.append(curr)
        else:
            stack.append([curr + numbers[idx], idx + 1])
            stack.append([curr - numbers[idx], idx + 1])
        # print(stack)
    # print(result)
    return result.count(target)


# 4트 - 재귀

# 재귀 참고 코드:::
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(
            numbers[1:], target + numbers[0]
        )


# print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
