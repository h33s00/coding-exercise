function capitalizeWords(arr) {
  let newArr = [];

  // 종료 조건

  if (arr.length === 0) return newArr;

  // Action

  newArr.push(arr[0].toUpperCase());

  newArr = newArr.concat(capitalizeWords(arr.slice(1)));

  return newArr;
}

console.log(capitalizeWords(["heesoo", "jiyeon"]));
