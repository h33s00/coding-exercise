from collections import deque

numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    d = deque(numbers)
    sum = 0

    def DFS(d, sum, target, sign):
        while len(d) > 0:
            sum += d.popleft() * sign

        if sum == target:
            return 1


print(solution(numbers, target))
