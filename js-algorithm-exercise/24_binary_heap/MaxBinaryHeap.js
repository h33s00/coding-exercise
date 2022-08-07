class MaxBinaryHeap {
  constructor() {
    this.values = [];
  }
  insert(val) {
    this.values.push(val);
    this.bubbleUp();
  }
  bubbleUp() {
    let idx = this.values.length - 1;
    const newVal = this.values[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.values[parentIdx];
      if (newVal <= parent) break;
      this.values[parentIdx] = newVal;
      this.values[idx] = parent;
      idx = parentIdx;
    }
  }
  extractMax() {
    // edge case
    if (this.values.length == 0) {
      return undefined;
    }
    if (this.values.length == 1) {
      return this.values.pop();
    }
    // swap the first value with the last one
    let newRoot = this.values.pop();
    this.values.push(this.values[0]);
    this.values[0] = newRoot;
    // pop the maximum value (ex-root)
    const maxVal = this.values.pop();
    this.sinkDown();
    return maxVal;
  }
  sinkDown() {
    let idx = 0;
    const length = this.values.length;
    const newRoot = this.values[0];
    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let leftVal, rightVal;
      let swap = null;

      if (leftIdx < length) {
        leftVal = this.values[leftIdx];
        if (leftVal > newRoot) {
          swap = leftIdx;
        }
      }
      if (rightIdx < length) {
        rightVal = this.values[rightIdx];
        if (
          (rightVal > newRoot && swap == null) ||
          (rightVal > newRoot && rightVal > leftVal)
        ) {
          swap = rightIdx;
        }
      }
      if (swap == null) break;

      this.values[idx] = this.values[swap];
      this.values[swap] = newRoot;
      idx = swap;
    }
  }
}

let mheap = new MaxBinaryHeap();
mheap.insert(3);
mheap.insert(7);
mheap.insert(9);
mheap.insert(2);
mheap.insert(10);
mheap.insert(4);
mheap.insert(5);

console.log(mheap.values);
