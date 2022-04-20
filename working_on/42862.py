# def solution(n, lost, reserve):
# students = [None]
# for i in range(1, n + 1):
#     print(i)
#     if i in lost and i in reserve:
#         students.append(1)
#     elif i in lost:
#         students.append(0)
#     elif i in reserve:
#         students.append(2)
#     else:
#         students.append(1)

# print(students)
# # students.append(None)

# return 0


def solution(n, lost, reserve):
    # 정렬되지 않은 상태라면,
    lost.sort()
    reserve.sort()
    og_reserve = reserve[:]
    print(f"도난당한 학생: {lost}")
    print(f"여벌이 있는 학생: {reserve}")

    # 도난 당하지 않은 학생 수
    answer = n - len(lost)
    print(f"나눔 전: {answer}")

    # 도난 당한 학생들에 대해,
    for student in lost:
        print("학생번호:", student)
        # 본인의 여벌이 있는 경우,
        if student in og_reserve:
            reserve.remove(student)
            answer += 1
            print("아 맞다!")
            print(answer, reserve)
        # 전 번호 학생이 여벌이 있는 경우,
        elif student - 1 in og_reserve:
            reserve.remove(student - 1)
            answer += 1
            print("끼얏호!")
            print(answer, reserve)
        # 다음 번호 학생이 여벌이 있는 경우,
        elif student + 1 in og_reserve:
            reserve.remove(student + 1)
            answer += 1
            print("끼얏호!")
            print(answer, reserve)
        else:
            print("어쩔 수 없지.")
        og_reserve = reserve

    return answer


# n, lost, reserve = 5, [2, 4], [1, 3, 5]
# n, lost, reserve = 5, [2, 4, 5], [1, 4]
# n, lost, reserve = 5, [2, 4], [3]
# n, lost, reserve = 3, [3], [1]
# n, lost, reserve = 3, [1, 2], [2, 3]
n, lost, reserve = 8, [3, 4, 7], [3, 5]
# n, lost, reserve = 2, [0], [0]
# n, lost, reserve = 12, [1, 2, 3, 4, 8, 9, 10, 12], [1]


# n, lost, reserve = 2, [1], [2]
# a = solution(n, lost, reserve)
# print(a)
print(solution(9, [5, 6, 8, 1, 2], [2, 3, 1, 4, 8, 9]))
