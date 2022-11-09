function countUniqueValues(sortedArr) {
  let i = 0;
  let k = 1;
  let uniqueVals = 0;
  while (i < sortedArr.length) {
    if (sortedArr[i] !== sortedArr[k]) {
      uniqueVals++;
      i = k;
      k = i + 1;
    } else {
      k++;
    }
  }
  return uniqueVals;
}

console.log(countUniqueValues([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])); // 7
