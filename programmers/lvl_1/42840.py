# 모의고사


def solution(answers):
    answer = []
    # 총 문제 수
    total = len(answers)
    # 수포자 채점표
    f = [1, 2, 3, 4, 5] * total
    s = [2, 1, 2, 3, 2, 4, 2, 5] * total
    t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * total
    students = [f, s, t]

    # 채점 시작
    grades = []
    for student in students:
        for i, a in enumerate(answers):
            if student[i] == a:
                student[i] = "Y"
            else:
                student[i] = "N"
        grades.append(student.count("Y"))

    # 1등 찾기
    top = max(grades)
    # 1등한 학생 수
    num_top = grades.count(top)

    for i in range(num_top):
        print(grades)
        m = grades.index(top)
        answer.append(m + 1)
        grades[m] = -1

    return answer


print(solution([1, 3, 2, 4, 2]))
