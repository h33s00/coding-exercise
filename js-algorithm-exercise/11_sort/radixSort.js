// my attempt
function getDigit(num, k) {
  return Math.floor((Math.abs(num) / Math.pow(10, k)) % 10);
}

function digitCount(num) {
  return num.toString().split("").length;
}

function maxDigit(num_arr) {
  let max = 0;
  for (e of num_arr) {
    if (digitCount(e) > max) max = digitCount(e);
  }
  return max;
}

function radixSort(num_arr) {
  let m = maxDigit(num_arr);
  // 한자릿수부터 쭉...
  for (let i = 0; i < m; i++) {
    console.log(`${i + 1}자릿수 run!`);
    let bucket = new Array(10);
    // 배열을 한번씩 방문!
    for (e of num_arr) {
      let spot = getDigit(e, i);
      if (typeof bucket[spot] == "undefined") {
        bucket[spot] = [e];
      } else {
        bucket[spot].push(e);
      }
    }
    console.log(bucket);

    // emptying the bucket
    // nums = [].concat(...bucket)
    let temp = [];
    for (let j = 0; j < 10; j++) {
      if (typeof bucket[j] != "undefined") {
        temp = temp.concat(bucket[j]);
      }
    }
    num_arr = temp;
  }

  return num_arr;
}

dummy = [9, 48294, 842, 4823, 21, 0];

// console.log(digitCount(48294));
// console.log(getDigit(9, 0));
// console.log(maxDigit(dummy));
console.log(radixSort(dummy));
