# 소수 찾기
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)

# def solution(n):
#     answer = 0  # 소수 카운트
#     for i in range(2, n + 1):
#         pos = []
#         # print(f"수 {i}를")
#         for k in range(2, i):
#             # print(f"{k}로 나눔 ")
#             # print(i % k)
#             if i % k == 0:  # 나누어진다?
#                 # print(f"{i}소수가 아닙니다!")
#                 pos.append(k)
#         if len(pos) == 0:  # 나누어질 수 있는 수가 하나도 없다면,
#             answer += 1

#     return answer


# print(solution(10))
# print(solution(5))


# 한번이라도 0으로 나누어 떨어진다면 소수가 아님!


def isPrime(n):
    if n == 1:
        return 0
    elif n == 2:
        print(n)
        return 1
    else:
        answer = 0
        for k in range(2, 10):
            if n % k == 0:
                break
            else:
                if k >= n - 1:
                    answer = 1
                    print(n)
                    break
                elif k == 9:
                    answer = 1
                    print(n)
                    break
        return answer


def solution(n):
    count = 0
    for i in range(2, n + 1):
        count = count + isPrime(i)
    return count


print(solution(1000))
# print(solution(5))
# print(solution(20))
