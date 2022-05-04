def solution(phone_book):
    answer = True
    pb_dic = {}
    for each in phone_book:
        pb_dic[each] = 0

    print(pb_dic)

    for each in phone_book:
        for i in range(len(each)):
            if each[:i] in pb_dic.keys():
                answer = False
                break

    return answer


# phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123", "456", "789"]
# phone_book = ["12", "123", "1235", "567", "88"]
print(solution(phone_book))
