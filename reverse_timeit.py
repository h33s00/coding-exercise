import timeit


def reverse(word):
    result = ""
    for i in range(-1, -len(word) - 1, -1):
        # print(word[i])
        result += word[i]
    return result


def reverse2(word):
    if len(word) == 1:
        return word
    else:
        return word[-1:] + reverse2(word[:-1])


testword = "dzissus" * 100
# print(testword)

# start1 = timeit.timeit()
# # reverse(testword)
# print(reverse(testword))
# end1 = timeit.timeit()
# print("루프 수행시간: ", (end1 - start1))

start2 = timeit.timeit()
# reverse2(testword)
print(reverse2(testword))
end2 = timeit.timeit()
print("재귀 수행시간: ", (end2 - start2))
