# 예산


def solution(d, budget):
    answer = 0
    if sum(d) <= budget:
        return len(d)
    else:
        d.sort()
        for amount in d:
            budget -= amount
            if budget < 0:
                break
            else:
                answer += 1

        return answer


d = [1, 3, 2, 5, 4]
budget = 9
# d = [2, 2, 3, 3];
# budget = 10;

a = solution(d, budget)
print(a)
