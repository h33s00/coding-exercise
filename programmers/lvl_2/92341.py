# 주차 요금 계산


from datetime import datetime
import math

# 이용시간을 분으로 변환
def convert(inTime, outTime):
    outT = datetime.strptime(outTime, "%H:%M")
    inT = datetime.strptime(inTime, "%H:%M")
    return int((outT - inT).total_seconds() // 60)


# print(convert("05:34", "07:59"))

# 같은 차량번호끼리 묶기 -> 딕셔너리
def calcFee(fees, car_r):
    calcResult = 0
    minutes = 0
    while len(car_r) > 0:
        # 기록이 페어가 아닌 하나만 남은 경우.
        # IN 기록만 존재하는 경우이다.
        if (len(car_r)) == 1:
            inTime = car_r[0][0]
            outTime = "23:59"
        # IN-OUT 짝으로 존재
        else:
            inTime = car_r[0][0]
            outTime = car_r[1][0]

        # 사용시간 분단위로 변환
        minutes += convert(inTime, outTime)
        del car_r[:2]

    print("총 사용시간: ", minutes)

    # 정산은 한꺼번에 이루어집니다.
    if minutes <= fees[0]:
        calcResult += fees[1]  # 기본 요금

    elif minutes > fees[0]:
        calcResult += fees[1] + math.ceil((minutes - fees[0]) / fees[2]) * fees[3]

    return calcResult


# print(
#     calcFee(
#         [180, 5000, 10, 600],
#         [["05:34", "IN"], ["07:59", "OUT"], ["22:59", "IN"], ["23:00", "OUT"]],
#     )
# )


def solution(fees, records):
    dict_records = {}
    answer = []

    for record in records:
        r = record.split(" ")
        if r[1] not in dict_records.keys():
            dict_records[r[1]] = [[r[0], r[2]]]
        else:
            dict_records[r[1]].append([r[0], r[2]])

    while len(dict_records) != 0:
        print(dict_records)
        car = min(dict_records.keys())
        car_r = dict_records[car]
        answer.append(calcFee(fees, car_r))
        del dict_records[car]

    return answer


# 기본 시간(분)	/ 기본 요금(원)	/ 단위 시간(분)	/ 단위 요금(원)
fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]
# [14600, 34400, 5000]

# fees = [120, 0, 60, 591]
# records = [
#     "16:00 3961 IN",
#     "16:00 0202 IN",
#     "18:00 3961 OUT",
#     "18:00 0202 OUT",
#     "23:58 3961 IN",
# ]
# # [0, 591]

# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]
# # [14841]


print(solution(fees, records))
