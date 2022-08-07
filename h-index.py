def solution(arr):
    n = len(arr)
    arr.sort(reverse=True)
    print(arr)

    if sum(arr) == 0:
        return 0

    lb = 0
    hb = 0

    for i, v in enumerate(arr):
        print(f"{v}이상인건 {i+1}개")

        # 중복인 값이 있는 경우 가장 마지막만 체크
        if i != n - 1 and arr[i + 1] == v:
            pass

        else:
            if i + 1 >= v:
                # 가능한 H-INDEX의 LOWER BOUND
                lb = [i, v]
                k = i
                # # 중복 아닌 그 직전 값을 찾는다.
                while arr[k] == lb[1]:
                    k -= 1
                    print(k)

                hb = [k, arr[k]]
                break

    print(lb, hb)

    return hb[0] + 1


# arr = [1, 3, 3, 0, 9, 9, 9, 2]
# arr = [3, 0, 6, 1, 5]
# arr = [3, 4, 5, 11, 15, 16, 17, 18, 19, 20]
arr = [22, 42]
# arr = [3, 3, 1, 0, 6, 5]
# arr = [10, 10, 10, 10, 10]
print(solution(arr))
