# 행렬의 덧셈


def solution(arr1, arr2):
    n = len(arr1)  # 행
    m = len(arr1[0])  # 열
    # print(n, m)
    answer = []
    for i in range(n):
        temp = []
        for k in range(m):
            temp.append(arr1[i][k] + arr2[i][k])
            # print(temp)
        answer.append(temp)
    return answer


# print(solution([[1],[2]], [[3],[4]]))
# print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
# print(solution([[1,3,6],[1,3,6]], [[3,4,4],[3,4,4]]))
