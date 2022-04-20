# 문자열 압축


def slicer(s, unit):
    slices = []
    back = ""
    count = 1

    for i in range(0, len(s), unit):
        curr = s[i : i + unit]
        print(f"인덱스: {i}")
        print(f"현재: {curr}")
        print(f"이전: {back}")
        print("--------------")

        try:

            if curr == back:
                count += 1

            else:
                # 첫 루프
                if i == 0:
                    continue

                elif count == 1:
                    slices.append(back)

                elif count > 1:
                    slices.append(str(count) + back)

                # 카운트 초기화
                count = 1

        finally:
            back = curr

        print(f"SLICES: {slices}")
        print(count)
        print("--------------")

    # 마지막 루프
    if count == 1:
        slices.append(back)
    else:
        slices.append(str(count) + back)

    return slices


def solution(s):
    answer = []
    if len(s) <= 1:
        return 1

    else:
        for unit in range(1, len(s)):
            answer.append(len("".join(slicer(s, unit))))

        print(f"후보: {answer}")

        return min(answer)


# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# s = "s"

a = solution(s)
print(a)
