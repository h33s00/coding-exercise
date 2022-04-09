# 비밀지도

# 1. 이진수를 표현한 문자열로 변환
def conversion(n, arr):
    new_arr = list(map(lambda x: format(x, "b"), arr))
    for i in range(n):
        if len(new_arr[i]) < n:
            new_arr[i] = "0" * (n - len(new_arr[i])) + new_arr[i]
    # 람다함수로도 표현가능
    # new_arr = list(
    #     map(lambda x: ("0" * (n - len(x))) + x if (len(x) < n) else x, new_arr)
    # )
    return new_arr


# 2. 해쉬태그와 공백으로의 변환
def solution(n, arr1, arr2):
    answer = []
    new_arr1 = conversion(n, arr1)
    print(new_arr1)
    new_arr2 = conversion(n, arr2)
    print(new_arr2)

    for i in range(n):
        temp = ""
        for j in range(n):
            # print(i, j)
            if new_arr1[i][j] == "0" and new_arr2[i][j] == "0":
                temp += " "
            else:
                temp += "#"
        print(temp)
        answer.append(temp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
