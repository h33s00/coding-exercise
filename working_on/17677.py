# 뉴스 클러스터링
# 50분 소요! 1트에 성공 :)

import string


def cleansing(str):
    # 1. 두 글자씩 끊어서 다중집합으로 정제
    # 2. 영문자만 유효
    # 3. 대소문자 구분 X

    # 모두 소문자로 바꿔준다
    s = list(str.lower())
    c = []

    alphabet = list(string.ascii_lowercase)
    for i in range(len(s)):
        # 두 글자씩 자르기
        couple = s[i : i + 2]
        if len(couple) == 2:
            if couple[0] in alphabet and couple[1] in alphabet:
                c.append("".join(couple))

    return c


def solution(str1, str2):
    a = cleansing(str1)
    b = cleansing(str2)
    # print(a, b)

    # 둘 다 공집합인 경우
    if len(a) == 0 and len(b) == 0:
        return int(1 * 65536)

    # A의 길이가 더 크다고 가정
    # if len(a) <= len(b):
    #     a, b = b, a

    inter = []

    # 교집합의 길이 구하기
    for item in set(a):
        if item in b:
            num_item = min(a.count(item), b.count(item))
            for i in range(num_item):
                inter.append(item)

    union = []

    # 합집합의 길이 구하기
    for item in set(a + b):
        num_item = max(a.count(item), b.count(item))
        print(num_item)
        for i in range(num_item):
            union.append(item)

    # J(A,B) = A,B 교집합 / A,B 합집합
    return int((len(inter) / len(union)) * 65536)


str1, str2 = "FRANCE", "french"
# str1, str2 = "handshake", "shake hands"
# str1, str2 = "aa1+aa2", "AAAA12"
# print(cleansing(str1))
# print(cleansing(str2))
print(solution(str1, str2))
