def solution3(n):
    if n == 1:
        return 0
    elif n == 2:
        print("2는 소수입니다.")
        return 1 + solution3(n - 1)
    else:
        answer = 0
        for k in range(2, 10):
            print(f"{n}%{k}")
            if n % k == 0:
                print(f"{n}은 소수가 아닙니다.")
                break
            else:
                if k == n - 1:
                    print(f"{n}은 소수입니다.")
                    answer += 1
        return answer + solution3(n - 1)


print(solution3(1000))
