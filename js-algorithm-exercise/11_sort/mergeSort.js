function mergeSort(arr) {
  function mergeArrays(arr1, arr2) {
    let result = [];
    let i = 0;
    let j = 0;
    while (i < arr1.length && j < arr2.length) {
      if (arr1[i] < arr2[j]) {
        result.push(arr1[i]);
        i += 1;
      } else {
        result.push(arr2[j]);
        j += 1;
      }
      // console.log(result);
      // console.log("i: ", i);
      // console.log("j: ", j);
    }

    // console.log(result);

    if (i == arr1.length) {
      result = result.concat(arr2.slice(j));
    } else if (j == arr2.length) {
      result = result.concat(arr1.slice(i));
    }

    return result;
  }

  if (arr.length <= 1) {
    return arr;
  }

  let midpoint = Math.floor(arr.length / 2);
  let left = mergeSort(arr.slice(0, midpoint));
  let right = mergeSort(arr.slice(midpoint));
  console.log(left);
  console.log(right);
  return mergeArrays(left, right);
}

// dummy = [];
// dummy.push([1], [2], [3]);
// console.log(dummy);
// dummy = [1, 8, 2, 0];
// dummy = [1, 0];
// dummy = [0];
dummy = [1, 9, 6];

// midpoint = Math.floor(dummy.length / 2);
// dummy2 = dummy.slice(0, midpoint);
// dummy3 = dummy.slice(midpoint);
// console.log(dummy2, dummy3);

console.log(mergeSort(dummy));
