// SAMPLE INPUT/OUTPUT
// recursiveRange(6) // 21
// recursiveRange(10) // 55

function recursiveRange(n) {
  if (n == 1) {
    return 1;
  } else {
    return n + recursiveRange(n - 1);
  }
}
