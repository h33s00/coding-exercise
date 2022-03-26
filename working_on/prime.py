# 소수 찾기
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)


def solution(n):
    answer = 0  # 소수 카운트
    for i in range(2, n + 1):
        pos = []
        # print(f"수 {i}를")
        for k in range(2, i):
            # print(f"{k}로 나눔 ")
            # print(i % k)
            if i % k == 0:  # 나누어진다?
                # print(f"{i}소수가 아닙니다!")
                pos.append(k)
        if len(pos) == 0:  # 나누어질 수 있는 수가 하나도 없다면,
            answer += 1

    return answer


# print(solution(10))
# print(solution(5))


def solution2(n):
    answer = 0
    if n == 1:
        return 0
    elif n == 2:
        print("2는 소수입니다.")
        return 1
    else:
        for k in range(2, n):
            print(f"{n}%{k}")
            if n % k == 0:
                print(f"{n}은 소수가 아닙니다.")
                break
            else:
                if k == n - 1:
                    print(f"{n}은 소수입니다.")
                    answer += 1
        return answer + solution2(n - 1)


# print(solution2(5))
# print(solution2(10))
# print(solution2(1000))
# print(solution2(2))
# print(solution2(3))

# 한번이라도 나누어 떨어진다면 소수가 아님!


def solution3(n):
    answer = 0
    if n == 1:
        return 0
    elif n == 2:
        print("2는 소수입니다.")
        return 1
    else:
        for k in range(2, 10):
            print(f"{n}%{k}")
            if n % k == 0:
                print(f"{n}은 소수가 아닙니다.")
                break
            else:
                if k == 9:
                    print(f"{n}은 소수입니다.")
                    answer += 1
        return answer + solution3(n - 1)


print(solution3(10))
