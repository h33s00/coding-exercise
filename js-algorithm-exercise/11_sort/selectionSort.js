function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let min = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) min = j;
    }
    // 최솟값이 나타났으면?
    if (i != min) {
      [arr[i], arr[min]] = [arr[min], arr[i]];
      console.log(arr);
    }
  }
  return arr;
}

// console.log(selectionSort([3, 5, 1, 5, 9]));
console.log(selectionSort([8, 1, 2, 3, 4, 5, 6, 7]));
