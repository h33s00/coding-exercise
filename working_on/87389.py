# 나머지가 1이 되는 수
def solution(n):
    # 나누어서 나머지가 1이 되는 제일 작은 자연수 x
    # 0과 자기자신은 x가 될 수 없다.
    # n이 3보다 크므로, 1도 x가 될 수 없다.
    for x in range(2, n):
        # print(x)
        if n % x == 1:
            return x
        else:
            continue


# print(solution(3))
# print(solution(4))
# print(solution(10))
# print(solution(12))
print(solution(1000))
