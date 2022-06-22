function capitalizeFirst(arr) {
  let newArr = [];

  // 종료 조건

  if (arr.length === 0) return newArr;

  // Action

  newArr.push(arr[0][0].toUpperCase() + arr[0].slice(1));

  newArr = newArr.concat(capitalizeFirst(arr.slice(1)));

  return newArr;
}

console.log(capitalizeFirst(["car", "taco", "banana"])); // ['Car','Taco','Banana']

// a = "car"[0].toUpperCase() + "car".slice(1);
// console.log(a);
