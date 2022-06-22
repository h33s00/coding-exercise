def quickSort(arr, start, end):
    start = 0
    end = len(arr)

    while start < end:
        pivotIdx = pivot(arr, start)

    # quickSort(arr, start, pivotIdx - 1)
    # quickSort(arr, pivotIdx + 1, end)

    return arr


def pivot(arr, start, end):
    pivotVal = arr[start]
    pivotIdx = start

    for i in range(1, end):
        print(arr)
        if pivotVal > arr[i]:
            pivotIdx += 1
            arr[i], arr[pivotIdx] = arr[pivotIdx], arr[i]
    arr[pivotIdx], arr[start] = arr[start], arr[pivotIdx]

    print(arr, pivotIdx)

    return pivotIdx


arr = [48, 0, 35, 32, 26, 27, 73]
quickSort(
    arr,
)
