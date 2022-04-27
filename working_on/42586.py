# 기능개발


def solution(progresses, speeds):
    answer = []

    while len(progresses) != 0:
        deploy = 0

        # 작업 진행
        for i in range(len(progresses)):
            # print(i)
            progresses[i] += speeds[i]
            # print(progresses)
            # print(speeds)

        # 배포 진행
        while len(progresses) != 0:
            if progresses[0] >= 100:  # 배포 가능!
                progresses.pop(0)
                speeds.pop(0)
                deploy += 1
            else:
                break

        if deploy != 0:
            answer.append(deploy)

    return answer


# progresses = [93, 30, 55]
progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 30, 5]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
