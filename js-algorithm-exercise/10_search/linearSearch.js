function linearSearch(array, value) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] == value) {
      return i;
    }
  }
  return -1;
}

// function linearSearch(array, value) {
//   for (i = 0; i < array.length; i++) {
//     if (array[i] == value) {
//       return i;
//     }
//     if (i == array.length - 1 && array[i] != value) {
//       return -1;
//     }
//   }
// }

// function linearSearch(array, value) {
//   answer = null;
//   array.forEach((e, i) => {
//     if (e === value) {
//       answer = i;
//     }
//   });

//   if (answer === null) {
//     answer = -1;
//   }
//   return answer;
// }

console.log(linearSearch([9, 8, 7, 6, 5], 8));
