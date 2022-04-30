#  튜플


def solution(s):
    answer = []
    temp = []
    # 문자열을 집합으로 바꿔준다
    s_set = slicer(s)
    # 총 갯수로 튜플의 요소 개수 판단
    s_length = len(s_set)
    print(s_length)

    for i in range(1, s_length + 1):
        for each in s_set:
            if len(each) == i:
                temp.append(each)

    for each in temp:
        for e in each:
            if e not in answer:
                answer.append(e)

    # 1부터 n 까지 순서로 요소의 순서 판단
    return answer


def slicer(s):
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    items = []
    s_list = list(s[1 : len(s) - 1])
    print(s_list)

    temp = ""
    el = []

    for i, v in enumerate(s_list):
        if v in number:
            temp += v
        if v == ",":
            el.append("".join(temp))
            temp = ""
        if v == "}":
            el.append("".join(temp))
            temp = ""
            items.append(el)
            el = []  # 하나의 배열의 끝

    print(items)

    result = []

    for item in items:
        if "" in item:
            item.remove("")
        result.append(list(map(int, item)))

    return result


# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{20,111},{111}}"
# s = [[20, 111], [111]]
# s = "{{123}}"
print(solution(s))
# print(slicer(s))
