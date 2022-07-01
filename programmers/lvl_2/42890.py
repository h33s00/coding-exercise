# 후보키
from itertools import combinations


# 최소성 만족 체크 함수
def minimality(setArr):
    i = 0
    for i in range(len(setArr)):
        for k in range(i + 1, len(setArr)):
            if setArr[i].issubset(setArr[k]):
                setArr[k] = {"v"}
        # print(setArr)

    return list(filter(({"v"}).__ne__, setArr))


# a = [{1, 2}, {1, 2, 3}, {1, 2, 4}, {1, 2, 5}]
# print(minimality(a))
# print(a[0] - a[1])
# print(a[1] - a[0])

# 중복값 체크 함수
def isDuplicate(arr):
    for each in arr:
        if arr.count(each) > 1:
            return True
    return False


# print(isDuplicate([[1, 2], [2, 4]]))

# 열 추출 함수
def get_col(relation, attrIndex):
    result = []
    for tuple in relation:
        result.append(list(map(lambda x: tuple[x], attrIndex)))
    return result


def solution(relation):
    answerSet = []
    # 속성의 개수
    numAttr = len(relation[0])
    # 속성의 인덱스로 속성을 구별한다.
    attrIndex = list(range(numAttr))
    # PK를 저장한다.
    pkIndex = []
    # print(attrIndex)

    for i in attrIndex:
        # 속성 하나로 후보키 존재?
        attr = [item[i] for item in relation]
        if not isDuplicate(attr):
            print(i, "is a primary key")
            pkIndex.append(i)

    # Unique Identifier를 제외한 집합에서
    for each in pkIndex:
        attrIndex.remove(each)

    # 후보키가 될 수 있는 집합을 찾는다.
    for n in range(2, len(attrIndex) + 1):
        for com in combinations(attrIndex, n):
            col = get_col(relation, list(com))
            if not isDuplicate(col):
                print(com, "is a unique identifier")
                answerSet.append(set(com))

    return len(pkIndex) + len(minimality(answerSet))


# relation = [
#     ["100", "ryan", "music", "2"],
#     ["200", "apeach", "math", "2"],
#     ["300", "tube", "computer", "3"],
#     ["400", "con", "computer", "4"],
#     ["500", "muzi", "music", "3"],
#     ["600", "apeach", "music", "2"],
# ]

# 반례 테케
relation = [
    ["a", "1", "aaa", "c", "ng"],
    ["a", "1", "bbb", "e", "g"],
    ["c", "1", "aaa", "d", "ng"],
    ["d", "2", "bbb", "d", "ng"],
]

print(solution(relation))
# print(get_col(relation, [0, 1, 3]))
