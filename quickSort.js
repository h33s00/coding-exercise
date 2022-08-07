function quickSort(arr, left = 0, right = arr.length - 1) {
  console.log(arr);
  console.log(left, right);
  //   종료조건?
  if (left < right) {
    let pivotIdx = pivot(arr, left, right);
    quickSort(arr, left, pivotIdx);
    quickSort(arr, pivotIdx + 1, right);
  }
  return arr;
}

function pivot(arr, start = 0, end = arr.length - 1) {
  let pv = arr[start];
  let pi = start;

  for (let i = start; i <= end; i++) {
    if (arr[i] < pv) {
      pi++;
      // SWAP!
      [arr[i], arr[pi]] = [arr[pi], arr[i]];
    }
  }
  //   PIVOT VALUE SWAP
  [arr[start], arr[pi]] = [arr[pi], arr[start]];
  console.log(arr);

  return pi;
}
input = [0, 1, 93, 8, 2, 4];
// console.log(pivot(input.slice(2)));
console.log(quickSort(input));
