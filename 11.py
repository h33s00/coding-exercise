# import heapq


def solution(A, B):
    sum = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        sum += A[i] * B[i]
        # print(sum)

    return sum


# A, B = [1, 4, 2], [5, 4, 4]
A, B = [1, 2], [3, 4]
solution(A, B)
