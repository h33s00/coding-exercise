# 같은 숫자는 싫어


def solution(arr):
    answer = []
    for item in arr:
        if len(answer) == 0:
            answer.append(item)
        elif answer[-1] != item:
            answer.append(item)

    return answer


# def solution(arr):
#     answer = []
#     for item in arr:
#         if item not in answer:
#             answer.append(item)
#         elif answer[-1] != item:
#             answer.append(item)

#     return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
