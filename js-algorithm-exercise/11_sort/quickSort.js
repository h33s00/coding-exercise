function quickSort(arr, left = 0, right = arr.length - 1) {
  // PIVOT 설정이 가능하게끔 DEFAULT VALUE
  function pivot(arr, start = 0, end = arr.length + 1) {
    // assigning pivot
    let pivot = arr[start];
    let swapIdx = start;
    console.log("THE PIVOT VALUE IS: ", pivot);
    //   where should the pivot be placed?
    //   in other words, how many values are smaller than pivot?
    for (let i = start + 1; i < arr.length; i++) {
      if (pivot > arr[i]) {
        console.log(arr);
        swapIdx++;
        [arr[i], arr[swapIdx]] = [arr[swapIdx], arr[i]];
      }
    }

    [arr[start], arr[swapIdx]] = [arr[swapIdx], arr[start]];

    return swapIdx;
  }
  // base case
  if (left < right) {
    let pivotIndex = pivot(arr, left, right);
    // left side
    quickSort(arr, left, pivotIndex - 1);
    // right side
    quickSort(arr, pivotIndex + 1, right);
  }

  return arr;
}

ex = [5, 2, 1, 8, 4, 7, 6, 3];
console.log(quickSort(ex));
