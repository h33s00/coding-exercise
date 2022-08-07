function mergeSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  let midpoint = Math.floor(arr.length / 2);
  console.log(arr.slice(0, midpoint));
  console.log(arr.slice(midpoint));
  let left = mergeSort(arr.slice(0, midpoint));
  let right = mergeSort(arr.slice(midpoint));

  return merge(left, right);
}

// 정렬된 두 배열을 합치는 함수
function merge(arr1, arr2) {
  let result = [];
  let i = 0;
  let j = 0;
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else {
      result.push(arr2[j]);
      j++;
    }
    console.log(result, i, j);
  }
  // exhausted?
  if (i == arr1.length) {
    // console.log(arr2.slice(j));
    result = result.concat(arr2.slice(j));
  } else if (j == arr2.length) {
    // console.log(arr1.slice(i));
    result = result.concat(arr1.slice(i));
  }

  return result;
}
input = [0, 1, 93, 8, 2, 4];
console.log(mergeSort(input));

// console.log(merge([0, 1, 93], [2, 4, 8]));
// console.log(merge([0], [2]));
