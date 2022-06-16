function binarySearch(sorted_arr, val) {
  let left = 0;
  let right = sorted_arr.length - 1;
  let middle = Math.floor((left + right) / 2);

  while (sorted_arr[middle] != val && left <= right) {
    console.log(left, middle, right);
    if (sorted_arr[middle] > val) {
      right = middle - 1;
    } else {
      left = middle + 1;
    }
    middle = Math.floor((left + right) / 2);
  }
  return sorted_arr[middle] == val ? middle : -1;
}

a = binarySearch([2, 5, 6, 9, 13, 15, 28, 30], 13);

console.log(a);
