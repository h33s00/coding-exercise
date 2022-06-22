#  H-INDEX


def solution(arr):
    n = len(arr)
    arr.sort(reverse=True)
    print(arr)

    # [하한선], [상한선]
    h_index = []

    # 예외: 0으로만 이루어진 배열의 경우 답은 항상 0
    if sum(arr) == 0:
        return 0

    # 1차 체크
    # 하한선 찾기
    for i, v in enumerate(arr):
        up = i + 1

        print(f"{v}이상인건 {up}개")

        # 중복이 있는 경우 마지막만 체크
        if i != n - 1 and arr[i + 1] == v:
            pass

        else:
            if up >= v:
                # 정답은 현재 값일 수도, 더 높을 수도 있음
                answer = v
                h_index.append([i, v])
                break

    # 1차 체크에서 조건을 만족하는 것이 없었다면 리턴
    if len(h_index) == 0:
        return len(arr)

    # 상한선 찾기
    i = h_index[0][0]
    while True:
        if arr[i] != h_index[0][1]:
            break
        i -= 1
    h_index.append([i, arr[i]])

    print(h_index)

    # 2차 체크
    # 하한선과 상한선 사이에서 최대 h값을 찾기
    for h in range(h_index[1][1] - 1, h_index[0][1] - 1, -1):
        print(h)
        if (h_index[0][0]) >= h:
            answer = h
            break

    return answer


# solution([3, 0, 6, 1, 5])
# solution([12, 11, 10, 9, 8, 1])
# solution([6, 6, 6, 6, 6, 1])
# print(solution([4, 4, 4]))
# solution([4, 4, 4, 5, 0, 1, 2, 3])
# print(solution([10, 11, 12, 13]))
# solution([0, 0, 1, 1])
# solution([0, 1])
solution([10, 9, 4, 1, 1])
# print(solution([31, 66]))
# print(solution([0, 0, 0]))
# solution([0, 1, 1])
# solution([0, 1, 2])
# solution([4, 3, 3, 3, 3])


# v 이상의 수가 i+1 개 만큼 존재함.
# 예) 1 이상의 수가 2 개 있다.
# h 이상의 수가 h 이상 존재해야 h 값이 된다.
