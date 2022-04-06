# 약수의 합


def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        answer = 1 + n  # 1과 자기 자신은 무조건 약수 :)
        for i in range(2, n):
            # 약수입니까?
            if n % i == 0:
                answer += i
        return answer


# print(solution(0))
print(solution(1))
print(solution(2))
# print(solution(12))
print(solution(5))
# print(solution(3000))
# print(solution(300000000000))
