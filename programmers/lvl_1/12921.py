# 소수 찾기


# 스스로 푼 단순한 풀이 (효율성 통과X)
# def solution(n):
#     if n == 2:
#         answer = 1
#     else:
#         answer = 2  # 2와 3은 소수입니다.
#         for i in range(3, n + 1):
#             for k in range(2, (i // 2) + 1):
#                 print(f"{i}%{k}")
#                 if i % k == 0:
#                     print(f"{i}은 소수가 아닙니다!")
#                     break
#                 else:
#                     if k == (i // 2):
#                         print(f"{i}은 소수입니다.")
#                         answer += 1
#     return answer

# 아리스토테레스의 체
# https://wikidocs.net/21638


def solution(n):
    # 0~N까지의 수(인덱스)를 준비한다.
    # 0, 1은 소수가 아니다. False, False 로 시작.
    sieve = [False, False] + [True] * (n - 1)
    for i in range(2, len(sieve)):
        print(f"수 {i}를 소수라고 가정하고,")
        # i만큼씩 증가하는 수 (i의 배수)
        # start, stop, step (i의 2배수부터 시작해서, 끝까지, i배증가)
        for k in range(2 * i, n + 1, i):
            print(f"{k}는 {i}의 배수이니 지웁시다.")
            sieve[k] = False
    answer = sieve.count(True)
    return answer


# print(solution(5))
# print(solution(10))
# print(solution(20))
print(solution(100))
# print(solution(1000))
