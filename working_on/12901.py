# 2016년


def solution(a, b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_of_days = sum(month[: a - 1]) + b
    print(num_of_days)
    index = (num_of_days % 7) - 1
    print(index)
    return day[index]


# print(solution(1, 1))
# print(solution(1, 2))
print(solution(1, 31))
print(solution(2, 1))
print(solution(2, 29))
# print(solution(1, 31))
print(solution(5, 24))
