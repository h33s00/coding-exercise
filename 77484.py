def countMatches(lottos, win_nums):
    count = 0
    for num in lottos:
        if num in win_nums:
            count += 1
    return count


def solution(lottos, win_nums):
    minMatches = countMatches(lottos, win_nums)
    unknown = lottos.count(0)
    # 나머지를 못 맞추었다고 가정하면 최저 순위.
    # 나머지를 모두 맞추었다고 가정하면 최고 순위.
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}  # 맞힌 숫자의 수: 순위
    answer = [rank[(minMatches + unknown)], rank[minMatches]]
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
