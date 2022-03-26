# 정수 제곱근 판별

import math


def solution(n):
    answer = 0
    x = math.sqrt(n)
    if int(x) == x:
        answer = int(math.pow(x + 1, 2))
    else:
        answer = -1
    return answer
