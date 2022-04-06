# 두 개 뽑아서 더하기


def solution(numbers):
    answer = []
    while len(numbers) != 0:
        std = numbers.pop()
        for item in numbers:
            answer.append(std + item)
    answer = list(set(answer))

    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
print(solution([0, 0]))
