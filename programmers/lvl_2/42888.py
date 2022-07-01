# 오픈채팅방


def solution(record):
    user_db = {}
    for each in record:
        arr = each.split(" ")
        if arr[0] == "Enter" or arr[0] == "Change":
            uid, nickname = arr[1], arr[2]

            if uid not in user_db:
                user_db[uid] = nickname
            else:
                if user_db[uid] != nickname:
                    user_db[uid] = nickname

    answer = []
    for each in record:
        arr = each.split(" ")
        if arr[0] == "Enter":
            answer.append(f"{user_db[arr[1]]}님이 들어왔습니다.")
        elif arr[0] == "Leave":
            answer.append(f"{user_db[arr[1]]}님이 나갔습니다.")

    return answer


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
print(solution(record))
