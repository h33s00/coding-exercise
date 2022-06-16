# first attempt
# def insertionSort(li):
#     for i in range(1, len(li)):
#         print(li)
#         # resets the bookmarked position
#         bkmk = i
#         # now looks at sorted array (left)
#         print("THE SORTED SIDE:", li[:bkmk], " // ", li[i])
#         for j in range(i - 1, -1, -1):
#             if li[i] < li[j]:
#                 bkmk = j

#         if bkmk != i:
#             li.insert(bkmk, li[i])
#             print(li)
#             li = li[: i + 1] + li[i + 2 :]

#     return li

# second attempt
# def insertionSort(li):
#     for i in range(1, len(li)):
#         # 별도로 저장
#         print(i)
#         currentVal = li[i]
#         print(li, "   //  ", currentVal)
#         for j in range(i - 1, -1, -1):
#             # print(i, j)
#             if li[j] > currentVal:
#                 li[j + 1] = li[j]
#                 print(li)
#                 li[j] = currentVal

#     return li


# optimized example
def insertionSort(arr):
    for i in range(1, len(arr)):
        curr = i
        # only loops if condition is met
        print(arr, arr[curr])
        while curr > 0 and arr[curr - 1] > arr[curr]:
            arr[curr - 1], arr[curr] = arr[curr], arr[curr - 1]
            curr -= 1
            print(arr)

    return arr


li = [2, 3, 0, 2, 1]
# li = [7, 2, 6, 1, 0]
print(insertionSort(li))
