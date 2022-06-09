function flatten(arr) {
  let newArr = [];

  // 종료 조건

  if (arr.length === 0) return newArr;

  // Action

  if (typeof arr[0] == "number") {
    newArr.push(arr[0]);
  } else {
    newArr = newArr.concat(flatten(arr[0]));
  }

  newArr = newArr.concat(flatten(arr.slice(1)));

  return newArr;
}

// console.log(flatten([1, 2, 3, [4, 5]])); // [1, 2, 3, 4, 5]
// console.log(flatten([1, [2, [3, 4], [[5]]]])); // [1, 2, 3, 4, 5]
console.log(flatten([[1], [2], [3]])); // [1,2,3]
