# 키패드 누르기


def distance(fr, to):
    x1, y1, x2, y2 = 0, 0, 0, 0
    phone = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
    for row in phone:
        if fr in row:
            x1 = row.index(fr)
            y1 = phone.index(row)
        if to in row:
            x2 = row.index(to)
            y2 = phone.index(row)
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance


# print(distance("1", "2"))
# print(distance("4", "2"))


def solution(numbers, hand):
    answer = ""
    loc_left = "*"
    loc_right = "#"
    for dial in numbers:
        dial = str(dial)
        print(f"왼손위치: {loc_left}, 오른손위치: {loc_right}")
        if dial in ["1", "4", "7"]:
            answer += "L"
            loc_left = dial
        elif dial in ["3", "6", "9"]:
            answer += "R"
            loc_right = dial
        else:
            print(dial, "을 누르려면 계산!!")
            use_left = distance(loc_left, dial)
            print(f"왼손을 쓰면: {use_left}")
            use_right = distance(loc_right, dial)
            print(f"오른손을 쓰면: {use_right}")

            if use_left == use_right:
                if hand == "right":
                    answer += "R"
                    loc_right = dial
                elif hand == "left":
                    answer += "L"
                    loc_left = dial
            else:
                if use_left < use_right:
                    answer += "L"
                    loc_left = dial
                else:
                    answer += "R"
                    loc_right = dial

    return answer


# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
