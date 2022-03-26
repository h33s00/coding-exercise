# 최대공약수와 최대공배수


def solution(n, m):
    if m < n:
        n, m = m, n

    # 최대공약수
    temp = []
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            temp.append(i)
    gcd = max(temp)

    # 최대공배수
    # 최대공약수를 이용하는 공식
    lcm = int(abs(n * m) / gcd)

    return [gcd, lcm]


# print(solution(3, 12))
# print(solution(12, 3))
print(solution(2, 5))
