# 나누어 떨어지는 숫자 배열


def solution(arr, divisor):
    answer = []
    for item in arr:
        if item % divisor == 0:
            answer.append(item)
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    # print(answer)

    return answer


# arr = [5, 9, 7, 10]
# arr = [2, 36, 1, 3]
arr = [3, 2, 6]

# divisor = 5
# divisor = 1
divisor = 10

solution(arr, divisor)
