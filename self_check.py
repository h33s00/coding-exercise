def duplicate_count(arr):
    result = []
    s = set(arr)
    for each in s:
        if arr.count(each) > 1:
            result.append(arr.count(each))

    if len(result) == 0:
        return -1
    else:
        return result


# arr = [1, 2, 3, 3, 3, 3, 4, 4]
arr = [1]
# arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
# arr = [3, 5, 7, 9, 1]
print(duplicate_count(arr))
