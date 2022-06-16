function bubbleSort(arr) {
  for (let i = arr.length - 1; i >= 0; i--) {
    for (let j = 0; j < i; j++) {
      console.log("step", i, j);
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        console.log(arr);
      }
    }
  }
  return arr;
}

// Optimized with noSwap
function bubbleSort(arr) {
  let noSwap;
  for (let i = arr.length - 1; i >= 0; i--) {
    noSwap = true;
    console.log(arr);
    for (let j = 0; j < i; j++) {
      // Swap
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        noSwap = false;
      }
    }
    if (noSwap) break;
  }
  return arr;
}

// console.log(bubbleSort([3, 5, 1, 5, 9]));
console.log(bubbleSort([8, 1, 2, 3, 4, 5, 6, 7]));
