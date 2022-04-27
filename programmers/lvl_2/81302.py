# 거리두기 확인하기

# 대기실 간에는 연관성이 없습니다. 고로 나눠서 작업합니다.


def distance_calc(p1, p2):
    # 맨해튼 거리를 반환합니다.
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def waiting_room(place):
    # 대기실 안 응시자들 위치를 저장하는 배열
    p_loc = []
    for i in range(5):
        for k in range(5):
            if place[i][k] == "P":
                p_loc.append([i, k])

    print("응시자 수: ", len(p_loc))

    # 응시자들 사이 맨해튼 거리 확인
    for i in range(len(p_loc)):
        for k in range(i + 1, len(p_loc)):
            p1 = p_loc[i]
            p2 = p_loc[k]
            if distance_calc(p1, p2) <= 1:
                return 0
            elif distance_calc(p1, p2) == 2:
                print("체크 진행 필요: ", p1, p2)
                # 1. 같은 행에 존재하는 경우
                if p1[0] == p2[0]:
                    # 두 사람 중간 칸 위치
                    if p1[1] > p2[1]:
                        p1, p2 = p2, p1
                    middle = p1[1] + 1
                    if place[p1[0]][middle] == "O":
                        return 0

                # 2. 같은 열에 존재하는 경우
                elif p1[1] == p2[1]:
                    # 두 사람 중간 칸 위치
                    if p1[0] > p2[0]:
                        p1, p2 = p2, p1
                    middle = p1[0] + 1
                    if place[middle][p1[1]] == "O":
                        return 0

                # 3. 대각선에 존재하는 경우
                else:
                    print("대각선!", p1, p2)

                    # 두 사람 중간 칸 위치 - 2칸
                    middle1 = [p1[0], p2[1]]
                    middle2 = [p2[0], p1[1]]

                    print(middle1)
                    print(middle2)

                    # 둘 사이 두칸 중 한칸이라도 테이블이라면,
                    if (
                        place[middle1[0]][middle1[1]] == "O"
                        or place[middle2[0]][middle2[1]] == "O"
                    ):
                        return 0

            else:
                pass
    return 1


def solution(places):
    answer = []
    for i in range(5):
        answer.append(waiting_room(places[i]))

    return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

# print(solution(places))


print(waiting_room(places[4]))

# print(waiting_room(["POPOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]))
