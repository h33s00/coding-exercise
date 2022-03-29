# 소수 찾기
# 소수를 효율적으로 찾는 방법을 알아봐야함!!!


def solution(n):
    if n == 2:
        answer = 1
    else:
        answer = 2  # 2와 3은 소수입니다.
        for i in range(3, n + 1):
            for k in range(2, (i // 2) + 1):
                print(f"{i}%{k}")
                if i % k == 0:
                    print(f"{i}은 소수가 아닙니다!")
                    break
                else:
                    if k == (i // 2):
                        print(f"{i}은 소수입니다.")
                        answer += 1
    return answer


# print(solution(5))
# print(solution(10))
# print(solution(20))
print(solution(1000))
