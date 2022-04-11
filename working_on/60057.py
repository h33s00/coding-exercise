# 문자열 압축


def solution(s):
    answer = 0
    # 연속단위 자르기
    c = []
    temp = []
    for i, v in enumerate(s):
        print(i)
        if i == len(s) - 1:
            c.append("".join(temp))
            print("끝!")
        else:
            if len(temp) == 0 or v == temp[-1]:
                temp.append(v)
                print(temp)
            else:
                c.append("".join(temp))
                print(c)
                temp = [v]

    print(c)

    return answer


a = solution("aabbaccc")
# print(a)
