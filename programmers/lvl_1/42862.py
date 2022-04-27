# 체육복


def solution(n, lost, reserve):
    # 정렬되지 않은 상태라면,
    lost = sorted(lost)
    reserve = sorted(reserve)
    og_lost = lost[:]
    og_reserve = reserve[:]

    # print(f"도난당한 학생: {lost}")
    # print(f"여벌이 있는 학생: {reserve}")

    # 도난 당했지만 여벌이 있는 학생은 다른 학생에게 빌려줄 수 없다.
    for student in og_lost:
        if student in og_reserve:
            reserve.remove(student)
            lost.remove(student)
        og_reserve = reserve
        og_lost = lost

    # 체육복이 있는 학생 수
    answer = n - len(lost)

    # 도난 당한 학생들에 대해,
    for student in lost:
        # print("학생번호:", student)
        # 전 번호 학생이 여벌이 있는 경우,
        if student - 1 in og_reserve:
            reserve.remove(student - 1)
            answer += 1
            # print("전!")
            # print(answer, reserve)
        # 다음 번호 학생이 여벌이 있는 경우,
        elif student + 1 in og_reserve:
            reserve.remove(student + 1)
            answer += 1
            # print("후!")
            # print(answer, reserve)
        og_reserve = reserve

    return answer


# n, lost, reserve = 5, [2, 4], [1, 3, 5]
# n, lost, reserve = 5, [2, 4, 5], [1, 4]
# n, lost, reserve = 5, [2, 4], [3]
# n, lost, reserve = 3, [3], [1]
# n, lost, reserve = 3, [1, 2], [2, 3]
# n, lost, reserve = 8, [3, 4, 7], [3, 5]
n, lost, reserve = 5, [1, 2, 4], [2, 3, 4, 5]
# n, lost, reserve = 2, [0], [0]
# n, lost, reserve = 12, [1, 2, 3, 4, 8, 9, 10, 12], [1]


# n, lost, reserve = 2, [1], [2]
a = solution(n, lost, reserve)
print(a)
